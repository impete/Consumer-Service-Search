#!/usr/bin/env python3
"""Coverage ratchet for tests/coverage-floor.json.

check:  fail if measured coverage is below the committed floor.
raise:  raise each floor by STEP points (never above the measured value or TARGET).
init:   set each floor to the measured value (initial baseline).
"""

import argparse
import json
import pathlib
import sys

FLOOR_FILE = pathlib.Path("tests/coverage-floor.json")
REPORT_DIR = pathlib.Path("tests/integration/testrpts")
STEP = 1.0
TARGET = 70.0


def measured():
    py = json.loads((REPORT_DIR / "coverage-python.json").read_text())
    ts = json.loads((REPORT_DIR / "api-coverage" / "coverage-summary.json").read_text())
    return {
        "python": round(py["totals"]["percent_covered"], 2),
        "typescript": round(ts["total"]["lines"]["pct"], 2),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["check", "raise", "init"])
    mode = parser.parse_args().mode
    now = measured()
    data = (
        json.loads(FLOOR_FILE.read_text())
        if FLOOR_FILE.exists()
        else {"python": None, "typescript": None}
    )
    floors = {k: data.get(k) for k in now}
    if mode == "check":
        if any(v is None for v in floors.values()):
            print("::warning::no coverage floor yet; baseline is set on merge to main")
            return 0
        bad = False
        for key, value in now.items():
            status = "ok" if value + 1e-9 >= floors[key] else "BELOW FLOOR"
            print(f"{key}: {value}% (floor {floors[key]}%) {status}")
            bad |= status != "ok"
        return 1 if bad else 0
    if mode == "init":
        floors = dict(now)
    else:
        floors = {
            k: (
                now[k]
                if floors[k] is None
                else round(max(floors[k], min(floors[k] + STEP, TARGET, now[k])), 2)
            )
            for k in now
        }
    FLOOR_FILE.write_text(json.dumps(floors, indent=2) + "\n")
    print(f"floors: {floors}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
