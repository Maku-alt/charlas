#!/usr/bin/env python3
"""Command-line validator for charla phase summaries."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


MODULE = Path(__file__).with_name("workflow_contract.py")
SPEC = importlib.util.spec_from_file_location("workflow_contract", MODULE)
workflow_contract = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow_contract)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True)
    parser.add_argument("--summary")
    parser.add_argument("--sentinel")
    parser.add_argument("--template")
    args = parser.parse_args()
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    if args.template:
        fields = workflow_contract.parse_summary(args.template)
        missing = [field for field in workflow_contract.REQUIRED_FIELDS if field not in fields]
        if missing:
            for field in missing:
                print(f"ERROR: Missing template field: {field}")
            return 1
        print("VALID TEMPLATE")
        return 0
    if not args.summary or not args.sentinel:
        parser.error("--summary and --sentinel are required unless --template is used")
    errors = workflow_contract._validate_summary(args.summary, contract, Path(args.sentinel))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
