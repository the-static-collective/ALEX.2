import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {researchPacket} from '../tools/motif021-search.mjs';
test('source-pinned local ALEX scan matches stored research packet byte-for-byte',()=>{
 const actual=researchPacket();
 const saved=JSON.parse(readFileSync(new URL('../research/packets/MOTIF-021/research-packet.json',import.meta.url)));
 assert.deepEqual(actual,saved);
 assert.equal(actual.source_inventory.length,5);
 assert.equal(actual.search_observation.coverage_status,'PARTIAL');
 assert.equal(actual.search_observation.result_count,actual.hits.length);
 assert.ok(actual.hits.every(h=>h.line_start>0&&h.git_blob.length===40));
});
test('source lines are search leads, not admitted real witness custody',()=>{
 const packet=researchPacket();
 assert.equal(packet.claim_status,'SOURCE_DISCOVERY_ONLY_NO_REAL_CUSTODY_AUTHENTICATED');
 assert.equal(packet.restrictions.evidence_admission,'NONE');
 assert.equal(packet.restrictions.permission_to_publish_private_data,false);
 assert.equal(packet.restrictions.independently_authenticated_custody,false);
 assert.ok(packet.coverage.every(x=>x.inspected_entire_materialized_source));
 assert.ok(packet.source_inventory.every(x=>x.source_commit.length===40));
});
