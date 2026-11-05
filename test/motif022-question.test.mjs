import test from 'node:test';
import assert from 'node:assert/strict';
import {ask,validate} from '../tools/motif022-question.mjs';
const q1='Which original carrier supports a suspected hidden common ancestor?';
const q2='How could independent reference witnesses suffer shared failures?';
const q3='Which source plans can compose a bounded GRAFT capability?';
test('three new questions select nonidentical pinned source lines',()=>{
 const all=[q1,q2,q3].map(x=>ask(x));
 assert.ok(all.every(x=>x.status==='RESEARCH_PACKET_HELD'));
 assert.ok(all.every(x=>x.hits.length>0));
 assert.notDeepEqual(all[0].hits,all[1].hits);
 assert.notDeepEqual(all[1].hits,all[2].hits);
 assert.ok(all.every(x=>validate(x)));
});
test('pinned source and line attribution survives ranked search',()=>{
 const x=ask(q1);
 assert.equal(x.source_count,5);
 assert.equal(x.partial_coverage,true);
 assert.equal(x.external_actions,0);
 assert.equal(x.real_independence_proved,false);
 assert.ok(x.hits.every(h=>h.source_commit.length===40&&h.source_blob.length===40&&h.line>0));
 assert.ok(x.coverage.every(s=>s.verified_git_blob.length===40));
});
test('out of corpus search holds, never fabricates sources',()=>{
 const x=ask('Can flibbergast quasarship make xyzzymorphs in squarzonium?');
 assert.equal(x.status,'HOLD_NO_MATCHES');
 assert.deepEqual(x.hits,[]);
});
test('bad question and tampering fail',()=>{
 assert.throws(()=>ask('hi'),/INVALID_QUESTION_LENGTH/);
 const p=ask(q1);
 assert.throws(()=>validate({...p,authority:'execute'}),/INVALID_ALEX/);
 assert.throws(()=>validate({...p,question:'forgery'}),/CHANGED_ALEX/);
});
test('deterministic question receipt',()=>assert.deepEqual(ask(q1),ask(q1)));
