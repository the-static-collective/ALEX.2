import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {eagleEye,validatePacket,SOURCE_LIMITS} from '../tools/eagle-eye-024.mjs';
const hash=b=>createHash('sha1').update(Buffer.from('blob '+b.length+'\0')).update(b).digest('hex');
const NAMES=['MOTIF','ALEX.2','JAR-VIS','planZ','GRAFT','the-daily-slice','MEMENTO'];
function mock({privateEntry=false,corrupt=false,githubFails=false,wikiFails=false}={}){
 const calls=[];
 const transport=async (url,opts)=>{
  const u=new URL(url); calls.push({url:u.href,method:opts.method,auth:!!opts.headers.Authorization});
  if(opts.method!=='GET')throw Error('unexpected write request');
  const fake=(data,status=200)=>({ok:status===200,status,redirected:false,json:async()=>data});
  if(u.hostname==='en.wikipedia.org'){
   if(wikiFails)return fake({error:'test'},503);
   return fake({query:{search:[{pageid:23,title:'Research methods',snippet:'<span>Methods</span> are not independent eyewitness evidence'}]}});
  }
  if(u.hostname==='api.openalex.org'){
   return fake({results:[{id:'https://openalex.org/W123',display_name:'Evidence-source provenance study',publication_year:2025,doi:'https://doi.org/10.1234/abcd'}]});
  }
  if(u.hostname!=='api.github.com')throw Error('unexpected host '+u.hostname);
  if(githubFails)return fake({},503);
  if(u.pathname==='/orgs/the-static-collective/repos'){
   return fake(NAMES.map((name,i)=>({
    full_name:'the-static-collective/'+name,
    owner:{login:'the-static-collective'},
    default_branch:'main',description:name==='JAR-VIS'?'attendant investigation research and source citations':
      name==='GRAFT'?'source graph composition research':
      name==='MOTIF'?'uncertainty provenance witness research':'experiment data and documents',
    topics:['research','source'], archived:false,private:privateEntry&&i===1,
    visibility:privateEntry&&i===1?'private':'public'
   })));
  }
  const match=u.pathname.match(/^\/repos\/the-static-collective\/([^/]+)\/(.+)$/);
  if(!match)return fake({},404);
  const name=match[1],route=match[2];
  const input=Buffer.from(name+' source research document. The witness provenance, source lineage and independent custody remain unresolved.');
  const sha=hash(input);
  if(route==='branches/main')return fake({commit:{sha:'a'.repeat(40)}});
  if(route==='git/commits/'+'a'.repeat(40))return fake({tree:{sha:'b'.repeat(40)}});
  if(route==='git/trees/'+'b'.repeat(40))return fake({truncated:false,tree:[
   {path:'README.md',sha,size:input.length,type:'blob'}]});
  if(route==='git/blobs/'+sha)return fake({encoding:'base64',size:input.length,
   content:(corrupt?Buffer.from(input+'!'):input).toString('base64')});
  return fake({},404);
 };
 return {transport,calls};
}
test('eagle eye is not confined to five originally allowed MOTIF repos',async()=>{
 const m=mock();
 const result=await eagleEye({question:'Which independent source lineage documents explain witness provenance?',
  scopes:{github:true,wikipedia:false,scholarly:false},depth:6},{transport:m.transport});
 assert.equal(result.status,'PUBLIC_RESEARCH_LEADS');
 assert.ok(result.catalog.enumerated>=7);
 assert.equal(result.catalog.selected,6);
 assert.equal(result.source_documents.length,6);
 assert.ok(result.hits.some(x=>x.kind==='github_source'&&x.source_commit==='a'.repeat(40)));
 assert.equal(result.authority,'none');
 assert.equal(result.private_sources_accessed,false);
 assert.equal(validatePacket(result),true);
 assert.ok(m.calls.every(x=>x.method==='GET'));
 assert.ok(m.calls.some(x=>x.url.includes('/orgs/the-static-collective/repos')));
});
test('public source code cannot be overread by a token that can see private repo',async()=>{
 const m=mock({privateEntry:true});
 const result=await eagleEye({question:'Which independent source lineage documents explain witness provenance?',
  scopes:{github:true,wikipedia:false,scholarly:false},depth:6},
  {transport:m.transport,githubToken:'not-an-actual-token'});
 assert.ok(result.source_documents.every(x=>x.repository!=='the-static-collective/ALEX.2'));
 assert.ok(m.calls.some(x=>x.auth));
 assert.equal(result.private_sources_accessed,false);
});
test('out-of-scope public providers require explicit opt-in, no query sent to them',async()=>{
 const m=mock();
 await eagleEye({question:'Which public source methods explain independent witness lineage?',
  scopes:{github:true,wikipedia:false,scholarly:false}}, {transport:m.transport});
 assert.ok(m.calls.every(x=>x.url.startsWith('https://api.github.com/')));
 const m2=mock();
 const r=await eagleEye({question:'How do research references explain source lineage?',
  scopes:{github:false,wikipedia:true,scholarly:true}}, {transport:m2.transport});
 assert.equal(r.providers.length,2);
 assert.ok(r.hits.some(x=>x.kind==='encyclopedia_index'));
 assert.ok(r.hits.some(x=>x.kind==='research_index'));
 assert.ok(m2.calls.every(x=>!x.auth));
 assert.ok(m2.calls.every(x=>x.url.includes('wikipedia.org')||x.url.includes('openalex.org')));
});
test('bad blob, provider failures and unsupported question do not fabricate evidence',async()=>{
 const broken=await eagleEye({question:'Which source documents establish witness custody?',
  scopes:{github:true,wikipedia:false,scholarly:false}},
  {transport:mock({corrupt:true}).transport});
 assert.equal(broken.status,'HOLD_NO_VERIFIED_LEADS');
 assert.equal(broken.source_documents.length,0);
 assert.ok(broken.failures.some(x=>/GIT_BLOB_INTEGRITY/.test(x.status)));
 const outage=await eagleEye({question:'Which source documents establish witness custody?',
  scopes:{github:true,wikipedia:true,scholarly:false}},
  {transport:mock({githubFails:true,wikiFails:true}).transport});
 assert.equal(outage.status,'HOLD_NO_VERIFIED_LEADS');
 assert.equal(outage.failures.length,2);
});
test('scope, depth and user question are bounded; no arbitrary hosts accepted',async()=>{
 const m=mock();
 await assert.rejects(eagleEye({question:'hi',scopes:{github:true}}),/INVALID_PUBLIC_QUESTION/);
 await assert.rejects(eagleEye({question:'Which sources should be inspected now?',scopes:{googleDrive:true}}),/NO_OPTED_IN|UNRECOGNIZED/);
 await assert.rejects(eagleEye({question:'Which sources should be inspected now?',scopes:{github:true},depth:999}),/UNBOUNDED_SOURCE_DEPTH/);
 assert.equal(SOURCE_LIMITS.repos,6);
 assert.equal(m.calls.length,0);
});
test('touched receipt or authority claim refuses validation',async()=>{
 const r=await eagleEye({question:'Which source documents establish witness custody?',
  scopes:{github:true,wikipedia:false,scholarly:false}},
  {transport:mock().transport});
 assert.throws(()=>validatePacket({...r,question:'modified'}),/TAMPERED_EAGLE_EYE/);
 assert.throws(()=>validatePacket({...r,authority:'publish'}),/INVALID_EAGLE_EYE/);
});
