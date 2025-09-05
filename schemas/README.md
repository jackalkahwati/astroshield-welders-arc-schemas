AstroShield Schema Index (SS0–SS6)

- SS0 (Heartbeat): schemas/ss0/heartbeat.status.schema.json
- SS1 (Detections): schemas/ss1/detection.raw.schema.json
- SS2 (Track): schemas/ss2/track.estimate.schema.json
- SS3 (Fusion): schemas/ss3/fusion.association.schema.json
- SS4 (State/Propagation): schemas/ss4/state.update.schema.json
- SS5 (Hostility/Proximity): schemas/ss5/*.schema.json
- SS6 (Decision/TEWA): schemas/ss6/decision.recommendation.schema.json

Notes:
- All messages carry schemaVersion, messageId, time*, producer, and provenance where applicable.
- Examples and validators are included where needed (see scripts/validate_ss5_message.py).



