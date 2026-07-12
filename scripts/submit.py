#!/usr/bin/env python3
"""Verify an exercise submission by running its pytest suite."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "exercises" / "submissions" / "registry.json"


def normalize_exercise_path(raw: str) -> Path:
    raw = raw.strip().rstrip("/")
    if raw.startswith("exercises/"):
        raw = raw[len("exercises/") :]
    path = ROOT / "exercises" / raw
    if not path.is_dir():
        raise SystemExit(f"Exercise not found: {path}")
    test_file = path / "test_solution.py"
    if not test_file.exists():
        raise SystemExit(f"No test_solution.py in {path}")
    return path


def load_registry() -> dict:
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {"submissions": []}


def save_registry(data: dict) -> None:
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def run_tests(exercise_path: Path) -> tuple[int, str]:
    test_file = exercise_path / "test_solution.py"
    cmd = [sys.executable, "-m", "pytest", str(test_file), "-q", "--tb=short"]
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output


def main() -> None:
    parser = argparse.ArgumentParser(description="Submit and verify an exercise.")
    parser.add_argument(
        "exercise",
        help="Exercise path, e.g. numpy/dot_product or exercises/pytorch/tensor_basics",
    )
    parser.add_argument(
        "--no-record",
        action="store_true",
        help="Run tests without updating submissions/registry.json",
    )
    args = parser.parse_args()

    exercise_path = normalize_exercise_path(args.exercise)
    rel = exercise_path.relative_to(ROOT / "exercises").as_posix()

    print(f"Verifying: exercises/{rel}")
    print("-" * 50)

    code, output = run_tests(exercise_path)
    print(output)

    passed = code == 0
    status = "passed" if passed else "failed"
    print("-" * 50)
    print(f"Result: {status.upper()}")

    if not args.no_record:
        registry = load_registry()
        entry = {
            "exercise": rel,
            "status": status,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        registry["submissions"] = [
            s for s in registry.get("submissions", []) if s.get("exercise") != rel
        ]
        registry["submissions"].append(entry)
        registry["submissions"].sort(key=lambda s: s["exercise"])
        save_registry(registry)
        print(f"Recorded in {REGISTRY.relative_to(ROOT)}")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
