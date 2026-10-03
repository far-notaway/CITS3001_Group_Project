#!/usr/bin/env python3
"""Check both accepted solutions on all sample and secret tests."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SOLUTIONS = sorted((ROOT / "submissions" / "accepted").glob("*.py"))


def normalise(data: bytes) -> bytes:
    return b" ".join(data.split())


def main() -> int:
    failures = 0
    checks = 0
    tests = sorted((ROOT / "data").glob("*/*.in"))
    for solution in SOLUTIONS:
        print(f"Trying {solution.name}")
        for input_path in tests:
            checks += 1
            answer_path = input_path.with_suffix(".ans")
            completed = subprocess.run(
                [sys.executable, str(solution)],
                input=input_path.read_bytes(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10,
                check=False,
            )
            ok = completed.returncode == 0 and normalise(completed.stdout) == normalise(answer_path.read_bytes())
            print(f"  {'PASS' if ok else 'FAIL'}  {input_path.relative_to(ROOT)}")
            failures += not ok
    print(f"\n{checks - failures}/{checks} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
