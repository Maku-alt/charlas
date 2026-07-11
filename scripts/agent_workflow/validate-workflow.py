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

ROLE_PATHS = {
    "orchestrator-charlas": "agents/orchestrator-charlas.md",
    "researcher-charlas": "agents/researcher-charlas.md",
    "narrative-charlas": "agents/narrative-charlas.md",
    "image-closer-charlas": "agents/image-closer-charlas.md",
    "deck-builder-charlas": "agents/deck-builder-charlas.md",
    "review-charlas": "agents/review-charlas.md",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--contract",
        default=str(Path(__file__).resolve().parents[2] / "agents" / "workflow-contract.json"),
    )
    parser.add_argument("--summary")
    parser.add_argument("--sentinel")
    parser.add_argument("--template")
    parser.add_argument("--check-phase-assets", action="store_true")
    args = parser.parse_args()
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    if args.check_phase_assets:
        errors: list[str] = []
        root = Path(args.contract).resolve().parent.parent
        phases = contract.get("phases", {})
        for phase_name, phase in phases.items():
            if phase_name == "release":
                if (
                    phase.get("role") != "orchestrator-charlas"
                    or phase.get("spec") != "embedded release contract"
                    or phase.get("prompt") != "not_applicable"
                ):
                    errors.append("Release must be an explicit orchestrator-owned embedded contract")
                continue

            role = phase.get("role")
            if not isinstance(role, str) or not role.strip():
                errors.append(f"Phase {phase_name} is missing a declared role")
            else:
                for role_name in role.split(" or "):
                    role_path = ROLE_PATHS.get(role_name)
                    if role_path is None or not (root / role_path).is_file():
                        errors.append(f"Phase {phase_name} references missing role: {role_name}")
            spec = phase.get("spec")
            if not isinstance(spec, str) or not spec.strip():
                errors.append(f"Phase {phase_name} is missing a declared spec")
            elif not (root / "templates" / "charlas-sdd" / "full" / spec).is_file():
                errors.append(f"Phase {phase_name} references missing spec: {spec}")
            prompt = phase.get("prompt")
            if prompt == "not_applicable":
                errors.append(f"Phase {phase_name} may use prompt not_applicable only for release")
            elif not isinstance(prompt, str) or not (root / "templates" / "charlas-sdd" / "prompts" / prompt).is_file():
                errors.append(f"Phase {phase_name} references missing prompt: {prompt}")

        for role_name, role in contract.get("auxiliary_roles", {}).items():
            required_flags = {
                "owns_phase": False,
                "may_modify_artifacts": False,
                "may_write_phase_summary": False,
                "may_approve": False,
                "may_block": False,
            }
            for field, expected in required_flags.items():
                if role.get(field) is not expected:
                    errors.append(f"Auxiliary role {role_name} must set {field} to {expected}")
            for field in ("role", "request_template", "prompt"):
                asset = role.get(field)
                if not isinstance(asset, str) or not (root / asset).is_file():
                    errors.append(f"Auxiliary role {role_name} references missing {field}: {asset}")
            if role_name in phases or any(role_name in phase.get("next", []) for phase in phases.values()):
                errors.append(f"Auxiliary role {role_name} must be absent from the phase transition graph")

        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        for role_name in contract.get("auxiliary_roles", {}):
            print(f"VALID AUXILIARY ROLE {role_name}")
            print(f"AUXILIARY ROLE {role_name} absent from phase transition graph")
        print("VALID ORCHESTRATOR RELEASE release")
        print("VALID PHASE ASSETS")
        return 0
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
