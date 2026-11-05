import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {investigatePublic,selectCollections,verifyPacket,AVAILABLE_COLLECTIONS}
 from '../tools/motif023-live.mjs';

const blob=b=>createHash('sha1').update(Buffer.from('blob '+b.length+'\0')).update(b).digest('hex');
const queryA='How could original Maxhinal Fiber and Pressure preserve source custody?';
const queryB='What can classical planZ and GRAFT compose into an executable capability?';
const origin='https://api.github.com/repos/';
function fakeApi({privateFirst=false,truncated=false,corrupt=false,disconnected=false}={}){
 const calls=[];
 const repos={
  'the-static-collective/ALEX.2':[
   ['README.md','ALEX source custody preserves original witnesses and independent evidence.'],
   ['docs/custody.md','Original source custody cannot be authenticated by repetition.']
  ],
  'the-static-collective/the-daily-slice':[
   ['README.md','MADD Maxhinal apparatus with old historical methods.'],
   ['artifacts/maxhinal/README.md','Fiber and Pressure are original Maxhinal chambers.']
  ],
  'the-static-collective/planZ':[
   ['README.md','planZ classical plan census and human review.'],
   ['docs/action.md','A classical plan can suggest next review actions.']
  ],
  'the-static-collective/GRAFT':[
   ['README.md','GRAFT executable capability composition remains review held.'],
   ['docs/compiler.md','Compose executable code only with owner review.']
  ],
  'the-static-collective/MOTIF':[
   ['README.md','MOTIF experiments on evidence, original methods and uncertainty.'],
   ['docs/question.md','Question receipts preserve source custody.']
  ]
 };
 const transport=async(url,init)=>{
  calls.push({url,method:init.method,authorization:!!init.headers.Authorization});
  const u=new URL(url);
  assert.equal(u.protocol,'https:');
  assert.equal(u.hostname,'api.github.com');
  assert.equal(init.method,'GET');
  const parts=u.pathname.split('/').filter(Boolean);
  const name=parts[1]+'/'+parts[2],items=repos[name];
  if(!items)return{ok:false,status:404,json:async()=>({message:'Not found'})};
  const ids=items.map(([path,text])=>{
   const bytes=Buffer.from(text);
   return{path,text,bytes,sha:blob(bytes),size:bytes.length};
  });
  const pos=parts.slice(3).join('/');
  let json;
  if(!pos){
   json={full_name:name,default_branch:'main',
    private:privateFirst&&name==='the-static-collective/ALEX.2',
    visibility:privateFirst&&name==='the-static-collective/ALEX.2'?'private':'public'};
  }else if(pos==='branches/main'){
   json={commit:{sha:'c'.repeat(40)}};
  }else if(pos==='git/commits/'+'c'.repeat(40)){
   json={tree:{sha:'d'.repeat(40)}};
  }else if(pos==='git/trees/'+'d'.repeat(40)){
   json={truncated,tree:ids.map(d=>({path:d.path,sha:d.sha,size:d.size,type:'blob'}))};
  }else if(pos.startsWith('git/blobs/')){
   const found=ids.find(x=>x.sha===pos.slice('git/blobs/'.length));
   if(!found)return{ok:false,status:404,json:async()=>({message:'Not found'})};
   const bytes=corrupt?Buffer.from(found.text+'!'):found.bytes;
   json={encoding:'base64',content:bytes.toString('base64'),size:found.size};
  }else{return{ok:false,status:404,json:async()=>({message:'Not found'})}}
  if(disconnected)return{ok:false,status:503,json:async()=>({message:'Unavailable'})};
  return{ok:true,status:200,json:async()=>json};
 };
 return{transport,calls};
}
test('explicitly selected NEW public collections are inspected at commit and blob, with page-like line loci',async()=>{
 const f=fakeApi();
 const packet=await investigatePublic({question:queryA,
  collections:['the-static-collective/ALEX.2','the-static-collective/the-daily-slice']},
  {transport:f.transport});
 assert.equal(packet.status,'HELD_SOURCE_RESEARCH_PACKET');
 assert.equal(packet.sources.length,2);
 assert.ok(packet.hits.some(x=>x.repository==='the-static-collective/the-daily-slice'));
 assert.ok(packet.hits.every(x=>x.source_commit==='c'.repeat(40)&&x.line>0));
 assert.ok(packet.sources.every(s=>s.public_eligibility_verified));
 assert.ok(f.calls.every(x=>x.method==='GET'));
 assert.ok(f.calls.some(x=>x.url.includes('/git/blobs/')));
 assert.equal(packet.source_custody_authenticated,false);
 assert.equal(packet.remote_writes,0);
 assert.equal(verifyPacket(packet),true);
});
test('question-driven source selection changes public collections',()=>{
 const one=selectCollections(queryA),two=selectCollections(queryB);
 assert.notDeepEqual(one.repositories,two.repositories);
 assert.ok(one.repositories.includes('the-static-collective/the-daily-slice'));
 assert.ok(two.repositories.includes('the-static-collective/GRAFT'));
 assert.ok(AVAILABLE_COLLECTIONS.includes('the-static-collective/MOTIF'));
});
test('authorized public read of a repo cannot silently enter private MEMENTO',()=>{
 assert.throws(()=>selectCollections(queryA,
 ['the-static-collective/MEMENTO']),/UNAUTHORIZED_SOURCE_COLLECTION/);
 assert.throws(()=>selectCollections(queryA,
 ['the-static-collective/ALEX.2','the-static-collective/ALEX.2']),/UNAUTHORIZED_SOURCE_COLLECTION/);
});
test('private visibility and truncated tree refuse entire source family',async()=>{
 const one=await investigatePublic({question:queryA,
  collections:['the-static-collective/ALEX.2']},
  {transport:fakeApi({privateFirst:true}).transport});
 assert.equal(one.status,'HOLD_NO_MATCHING_VERIFIED_SOURCE');
 assert.equal(one.sources.length,0);
 assert.match(one.errors[0].reason,/NOT_VERIFIED_PUBLIC/);
 const two=await investigatePublic({question:queryA,
  collections:['the-static-collective/the-daily-slice']},
  {transport:fakeApi({truncated:true}).transport});
 assert.equal(two.sources.length,0);
 assert.match(two.errors[0].reason,/TRUNCATED_SOURCE_TREE/);
});
test('changed blob bytes produce refusal instead of invented source citations',async()=>{
 const packet=await investigatePublic({question:queryA,
  collections:['the-static-collective/the-daily-slice']},
  {transport:fakeApi({corrupt:true}).transport});
 assert.equal(packet.sources.length,0);
 assert.equal(packet.hits.length,0);
 assert.match(packet.errors[0].reason,/CHANGED_SOURCE_BLOB|OVERSIZE_BLOB/);
});
test('disconnected source is incomplete coverage, not evidence the source does not exist',async()=>{
 const p=await investigatePublic({question:queryA,
  collections:['the-static-collective/ALEX.2']},
  {transport:fakeApi({disconnected:true}).transport});
 assert.equal(p.sources.length,0);
 assert.equal(p.status,'HOLD_NO_MATCHING_VERIFIED_SOURCE');
 assert.equal(p.errors.length,1);
 assert.equal(p.independent_origins_authenticated,false);
});
test('receipt integrity refuses changed question or claimed source admission',async()=>{
 const p=await investigatePublic({question:queryA,
  collections:['the-static-collective/ALEX.2']},
  {transport:fakeApi().transport});
 assert.throws(()=>verifyPacket({...p,question:'new'}),/TAMPERED/);
 assert.throws(()=>verifyPacket({...p,evidence_admission:'YES'}),/INVALID/);
 assert.throws(()=>verifyPacket({...p,private_material_accessed:true}),/INVALID/);
});
