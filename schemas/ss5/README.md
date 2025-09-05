SS5 Schemas (StarDrive | AstroShield)

Topics and artifacts:
- Trigger: `ss5.proximity.encounter` → schemas/ss5/proximity.encounter.schema.json
- Output: `ss5.separation.detected` → schemas/ss5/separation.detected.schema.json
- Output: `ss5.maneuver.detected` → schemas/ss5/maneuver.detected.schema.json
- Output: `ss5.launch.detected` → schemas/ss5/launch.detected.schema.json

Mode-1 Test Steps:
1) Publish a valid `ss5.proximity.encounter` to the designated test topic.
2) Expect `ss5.separation.detected` with Pc/missDistance/thresholds and provenance.
3) Optional: publish maneuver/launch detections per services.

Kafka Notes:
- JSON payloads initially; Avro optional if required by the cohort.
- Provenance ties to `manifestId` from AstroShield run manifest, plus gitSha/containerDigest.

POC:
- Primary: StarDrive AstroShield Integration (email on file)
- Backup: Engineering Lead (email on file)



