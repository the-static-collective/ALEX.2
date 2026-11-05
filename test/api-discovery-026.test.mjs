import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {identifyGap,inspectSpec,discoverMissingProvider,verifyDiscovery,DISCOVERY_LIMITS}
 from '../tools/api-discovery-026.mjs';

const commit='a'.repeat(40),tree='b'.repeat(40),repo='public-weather/weather-openapi';
const spec={openapi:'3.0.3',info:{title:'Public Weather Example',version:'1.0'},
 servers:[{url:'https://data.weather.example/v1'},{url:'http://127.0.0.1/admin'}],
 paths:{'/forecast':{get:{summary:'Read hourly forecast',
  parameters:[{name:'latitude',in:'query',required:true}]}}}};
const bytes=Buffer.from(JSON.stringify(spec));
const blob=b=>createHash('sha1').update(Buffer.from('blob '+b.length+'\0')).update(b).digest('hex');
const specHash=blob(bytes);
const Q='Which live weather forecast API provides hourly weather data?';
function mock({privateRepo=false,corrupt=false,searchDown=false,yamlOnly=false}={}){
 const calls=[];
 const transport=async (url,init)=>{
  const u=new URL(url);calls.push({url:u.href,method:init.method,host:u.hostname});
  assert.equal(u.hostname,'api.github.com');
  assert.equal(init.method,'GET');
  const ok=data=>({ok:true,status:200,redirected:false,json:async()=>data});
  const fail=status=>({ok:false,status,redirected:false,json:async()=>({message:'test fail'})});
  if(u.pathname==='/search/repositories'){
   if(searchDown)return fail(503);
   return ok({items:[{private:false,visibility:'public',full_name:repo,default_branch:'main'}],
    total_count:1});
  }
  if(u.pathname==='/repos/'+repo)
   return ok({private:privateRepo,visibility:privateRepo?'private':'public',
    full_name:repo,default_branch:'main'});
  if(u.pathname==='/repos/'+repo+'/branches/main')
   return ok({commit:{sha:commit}});
  if(u.pathname==='/repos/'+repo+'/git/commits/'+commit)
   return ok({tree:{sha:tree}});
  if(u.pathname==='/repos/'+repo+'/git/trees/'+tree)
   return ok({truncated:false,tree:[
    {path:yamlOnly?'openapi.yaml':'openapi.json',sha:specHash,size:bytes.length,type:'blob'}
   ]});
  if(u.pathname==='/repos/'+repo+'/git/blobs/'+specHash)
   return ok({encoding:'base64',size:bytes.length,
    content:(corrupt?Buffer.from(bytes.toString()+'!'):bytes).toString('base64')});
  return fail(404);
 };
 return {transport,calls};
}
test('weather question identifies a specialized gap rather than claiming any seven existing indexes are live weather sources',()=>{
 const g=identifyGap(Q);
 assert.equal(g.status,'NEEDS_SPECIALIZED_SOURCE');
 assert.equal(g.identified_domain,'weather');
 assert.equal(g.approval_to_contact_candidate_host,false);
});
test('operator public-search approval is required before even GitHub search',async()=>{
 const m=mock();
 const result=await discoverMissingProvider({question:Q},{transport:m.transport});
 assert.equal(result.status,'HOLD_PUBLIC_DISCOVERY_NOT_APPROVED');
 assert.equal(result.origin_searches_executed,0);
 assert.equal(m.calls.length,0);
 assert.equal(verifyDiscovery(result),true);
});
test('GitHub discovers a NEW API spec, pins blob & commit, proposes GET without contacting advertised server',async()=>{
 const m=mock();
 const p=await discoverMissingProvider({question:Q,approvedPublicGithubSearch:true},{transport:m.transport});
 assert.equal(p.status,'PROPOSED_NEW_PUBLIC_SOURCE_ADAPTER');
 assert.equal(p.candidate_repositories_screened,1);
 assert.equal(p.public_provider_proposals.length,1);
 const c=p.public_provider_proposals[0];
 assert.equal(c.repository,repo);
 assert.equal(c.git_blob,specHash);
 assert.equal(c.source_commit,commit);
 assert.equal(c.operation.method,'GET');
 assert.equal(c.operation.path,'/forecast');
 assert.deepEqual(c.declared_servers,['https://data.weather.example/v1']);
 assert.equal(c.service_endpoint_tested,false);
 assert.equal(c.production_permissions,'NONE');
 assert.equal(p.no_candidate_endpoint_contact,true);
 assert.ok(m.calls.every(x=>x.host==='api.github.com'&&x.method==='GET'));
 assert.equal(verifyDiscovery(p),true);
});
test('private visibility and changed original blob fail closed',async()=>{
 for(const options of [{privateRepo:true},{corrupt:true}]){
  const m=mock(options);
  const p=await discoverMissingProvider({question:Q,approvedPublicGithubSearch:true},{transport:m.transport});
  assert.equal(p.status,'HOLD_NO_REVIEWABLE_OPENAPI_SPEC');
  assert.equal(p.public_provider_proposals.length,0);
  assert.equal(p.no_candidate_endpoint_contact,true);
  assert.ok(p.errors.length);
  assert.equal(verifyDiscovery(p),true);
 }
});
test('YAML spec can be discovered without falsely declaring complete JSON schema parsing',async()=>{
 const p=await discoverMissingProvider({question:Q,approvedPublicGithubSearch:true},
  {transport:mock({yamlOnly:true}).transport});
 assert.equal(p.status,'HOLD_NO_REVIEWABLE_OPENAPI_SPEC');
 assert.equal(p.unreviewed_spec_documents[0].format,'yaml');
 assert.equal(p.yaml_sources_not_parsed_as_json,true);
});
test('unknown domain, unsafe spec and mutable receipt cannot be promoted',async()=>{
 const m=mock();
 const p=await discoverMissingProvider({question:'What is the meaning of graceful rainbows?',
  approvedPublicGithubSearch:true},{transport:m.transport});
 assert.equal(p.status,'HOLD_UNRECOGNIZED_DOMAIN');
 assert.equal(m.calls.length,0);
 assert.throws(()=>inspectSpec(Buffer.from('{"hello":1}'),
  {repo,commit,path:'openapi.json',git_blob:blob(Buffer.from('{"hello":1}'))}),/NOT_VALID_OPENAPI3/);
 const good=await discoverMissingProvider({question:Q,approvedPublicGithubSearch:true},
  {transport:m.transport});
 assert.throws(()=>verifyDiscovery({...good,status:'ADMITTED'}),/TAMPERED/);
 assert.throws(()=>verifyDiscovery({...good,authority:'deploy'}),/INVALID/);
});
test('discovery budgets and exact source constraints are explicit',()=>{
 assert.ok(DISCOVERY_LIMITS.requests<=18);
 assert.ok(DISCOVERY_LIMITS.inspectRepos<=3);
 assert.ok(DISCOVERY_LIMITS.bytes<=36000);
});
