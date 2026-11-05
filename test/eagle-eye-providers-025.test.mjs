import test from 'node:test';
import assert from 'node:assert/strict';
import {
 discoverProviders,searchSelectedProviders,verifySupplemental,PUBLIC_PROVIDER_CATALOG
} from '../tools/eagle-eye-providers-025.mjs';

const questions={
 code:'Which public GitHub repositories have executable source-code implementations?',
 paper:'Which scholarly papers examine correlated witness errors and independent evidence?',
 book:'Which books explain natural philosophy and ancient history?',
 medicine:'Which biomedical publications study clinical cancer genetics?'
};
function mock(overrides={}){
 const requests=[];
 const transport=async (url,init)=>{
  const u=new URL(url);
  requests.push({host:u.hostname,url:u.href,method:init.method,auth:!!init.headers.Authorization});
  if(init.method!=='GET')throw Error('write attempted');
  if(u.hostname==='api.crossref.org')return {ok:!overrides.crossrefDown,status:overrides.crossrefDown?503:200,
   json:async()=>({message:{items:[{DOI:'10.1234/teststudy',title:['A scholarly paper on shared errors'],
    published:{'date-parts':[[2025,1,1]]}}]}})};
  if(u.hostname==='openlibrary.org')return {ok:true,status:200,
   json:async()=>({docs:[{key:'/works/OL12345W',title:'Studies of ancient philosophy',
    author_name:['Aristotle'],first_publish_year:1900}]})};
  if(u.hostname==='www.ebi.ac.uk')return {ok:true,status:200,
   json:async()=>({resultList:{result:[{id:'123456',source:'MED',
    title:'Biomedical clinical genetics',pubYear:'2024',
    authorString:'Smith A',doi:'10.5678/biomed'}]}})};
  if(u.hostname==='api.github.com')return {ok:true,status:200,
   json:async()=>({items:[{private:false,full_name:'public-lab/open-code',
    description:'Source code matching the requested topics'},
    {private:true,full_name:'secret-lab/private-code',description:'NOT ELIGIBLE'}]})};
  throw Error('unexpected host');
 };
 return {requests,transport};
}
test('question-aware routes distinguish code, books, medical studies and scholarship without making a network call',()=>{
 const all=Object.fromEntries(Object.entries(questions).map(([k,q])=>[k,discoverProviders(q)]));
 assert.ok(all.code.recommended.includes('githubglobal'));
 assert.ok(all.book.recommended.includes('openlibrary'));
 assert.ok(all.medicine.recommended.includes('europepmc'));
 assert.ok(all.paper.recommended.includes('crossref'));
 assert.ok(all.paper.recommended.includes('scholarly'));
 assert.equal(all.code.no_remote_request,true);
 assert.equal(all.book.explicit_operator_source_selection_required,true);
 assert.equal(PUBLIC_PROVIDER_CATALOG.length,7);
});
test('selected providers are contacted by GET once, none others',async()=>{
 const m=mock();
 const p=await searchSelectedProviders({question:questions.book,
  scopes:{openlibrary:true,crossref:false}},{transport:m.transport});
 assert.equal(p.status,'PUBLIC_INDEX_LEADS');
 assert.equal(p.hits[0].provider,'openlibrary');
 assert.equal(p.hits[0].url,'https://openlibrary.org/works/OL12345W');
 assert.deepEqual(m.requests.map(x=>x.host),['openlibrary.org']);
 assert.equal(verifySupplemental(p),true);
});
test('github global search filters private repositories even if token could see them',async()=>{
 const m=mock();
 const p=await searchSelectedProviders({question:questions.code,
  scopes:{githubglobal:true}},{transport:m.transport,githubToken:'not-real'});
 assert.equal(p.hits.length,1);
 assert.equal(p.hits[0].provider,'githubglobal');
 assert.equal(p.hits[0].url,'https://github.com/public-lab/open-code');
 assert.ok(m.requests[0].auth);
 assert.equal(p.private_sources_accessed,false);
});
test('Crossref, Europe PMC return DOI metadata leads, not full papers',async()=>{
 const m=mock();
 const p=await searchSelectedProviders({question:questions.medicine,
  scopes:{crossref:true,europepmc:true}},{transport:m.transport});
 assert.equal(p.hits.length,2);
 assert.ok(p.hits.every(x=>x.url.startsWith('https://doi.org/')));
 assert.ok(p.hits.every(x=>x.provenance.includes('NOT_')||x.provenance.includes('METADATA')));
 assert.equal(p.source_independence_verified,false);
 assert.equal(verifySupplemental(p),true);
});
test('provider failure is isolated; remaining selected provider can still return results',async()=>{
 const m=mock({crossrefDown:true});
 const p=await searchSelectedProviders({question:questions.paper,
  scopes:{crossref:true,openlibrary:true}},{transport:m.transport});
 assert.equal(p.status,'PUBLIC_INDEX_LEADS');
 assert.ok(p.failures.some(x=>x.provider==='crossref'));
 assert.ok(p.hits.some(x=>x.provider==='openlibrary'));
});
test('unknown scope, missing consent and excess provider count are HOLD, with no outbound traffic',async()=>{
 const m=mock();
 await assert.rejects(searchSelectedProviders({question:questions.code,
  scopes:{myDrive:true}},{transport:m.transport}),/UNKNOWN_SOURCE_SCOPE/);
 await assert.rejects(searchSelectedProviders({question:questions.code,
  scopes:{}},{transport:m.transport}),/SOURCE_LIMIT_OR_CONSENT/);
 await assert.rejects(searchSelectedProviders({question:questions.code,
  scopes:{github:true,wikipedia:true,scholarly:true,openlibrary:true,crossref:true}},
  {transport:m.transport}),/SOURCE_LIMIT_OR_CONSENT/);
 assert.equal(m.requests.length,0);
});
test('forged evidence, altered DOI or changed receipt is explicitly refused',async()=>{
 const m=mock(),p=await searchSelectedProviders({question:questions.paper,
  scopes:{crossref:true}},{transport:m.transport});
 assert.throws(()=>verifySupplemental({...p,authority:'publish'}),/INVALID/);
 assert.throws(()=>verifySupplemental({...p,question:'changed'}),/TAMPERED/);
 const h={...p.hits[0],url:'https://example.org/hidden'};
 const {checksum_sha256,...body}=p;
 // Even with an attacker changing the result object, the original checksum fails.
 assert.throws(()=>verifySupplemental({...p,hits:[h]}),/TAMPERED/);
});
test('existing providers do not get queried by supplemental router',async()=>{
 const m=mock();
 const p=await searchSelectedProviders({question:questions.code,
   scopes:{github:true,wikipedia:true}},{transport:m.transport});
 assert.equal(p.status,'NO_SUPPLEMENTAL_PROVIDERS_SELECTED');
 assert.deepEqual(p.providers_queried,[]);
 assert.equal(m.requests.length,0);
});
