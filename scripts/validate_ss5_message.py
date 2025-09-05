#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator


def load_schema(name: str) -> dict:
    here = Path(__file__).parent.parent / "schemas" / "ss5" / f"{name}.schema.json"
    return json.loads(here.read_text())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("schema", help="schema name, e.g., separation.detected")
    ap.add_argument("payload", type=Path, help="path to JSON payload")
    args = ap.parse_args()

    schema = load_schema(args.schema)
    payload = json.loads(args.payload.read_text())
    Draft202012Validator(schema).validate(payload)
    print("OK")


if __name__ == "__main__":
    main()




