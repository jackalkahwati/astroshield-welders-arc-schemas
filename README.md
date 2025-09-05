Description

Schemas for StarDrive | AstroShield SS0–SS6 (Welders Arc). Includes SS5 Mode-1 example and CI validation.

Versioning

Semantic versioning. Tag vMAJOR.MINOR.PATCH; breaking changes bump MAJOR.

CI

GitHub Actions validates example payloads against schemas on push/PR.

AstroShield Welders Arc Schemas (SS0–SS6)

- SS0: schemas/ss0/heartbeat.status.schema.json
- SS1: schemas/ss1/detection.raw.schema.json
- SS2: schemas/ss2/track.estimate.schema.json
- SS3: schemas/ss3/fusion.association.schema.json
- SS4: schemas/ss4/state.update.schema.json
- SS5: schemas/ss5/*.schema.json (examples in schemas/ss5/examples/)
- SS6: schemas/ss6/decision.recommendation.schema.json

Validator:
- scripts/validate_ss5_message.py

License: Apache-2.0 (adjust if needed)
