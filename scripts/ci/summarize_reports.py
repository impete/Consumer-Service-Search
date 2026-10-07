#!/usr/bin/env python3
"""Print a markdown summary of the JUnit and coverage reports in tests/*/testrpts."""

import json
import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path("tests")


def junit_totals(path):
    totals = dict(tests=0, failures=0, errors=0, skipped=0)
    for suite in ET.parse(path).getroot().iter("testsuite"):
        for key in totals:
            totals[key] += int(suite.get(key, 0))
    return totals


def main():
    print("<!-- test-reports -->")
    print("### Test results\n")
    print("| Suite | Report | Tests | Failed | Errors | Skipped |")
    print("|---|---|---|---|---|---|")
    found = False
    for path in sorted(ROOT.glob("*/testrpts/*junit*.xml")):
        t = junit_totals(path)
        found = True
        print(
            f"| {path.parts[1]} | `{path.name}` | {t['tests']} | {t['failures']} | "
            f"{t['errors']} | {t['skipped']} |"
        )
    if not found:
        print("| _no reports_ | | | | | |")
    floor_file = ROOT / "coverage-floor.json"
    floors = json.loads(floor_file.read_text()) if floor_file.exists() else {}
    rpts = ROOT / "integration" / "testrpts"
    print("\n### Coverage\n")
    print("| Area | Coverage | Floor |")
    print("|---|---|---|")
    py = rpts / "coverage-python.json"
    ts = rpts / "api-coverage" / "coverage-summary.json"
    if py.exists():
        pct = round(json.loads(py.read_text())["totals"]["percent_covered"], 2)
        print(f"| `apps/search-service/app/` | {pct}% | {floors.get('python')} |")
    if ts.exists():
        pct = json.loads(ts.read_text())["total"]["lines"]["pct"]
        print(
            f"| `apps/api/src/` (excl. `server.ts`) | {pct}% | {floors.get('typescript')} |"
        )


if __name__ == "__main__":
    main()
