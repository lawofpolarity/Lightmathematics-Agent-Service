"""LM-AGENT-SERVICE-001 v1.0.0 contract smoke tests.

These tests validate frozen decision-state handling only. They are not evidence
of LM-specific superiority and are not a substitute for the strong comparator.
"""

def decide(evidence, dependency, authority, current, unresolved):
    if evidence is False or authority is False:
        return "REFUSE"
    if current is False:
        return "STALE"
    if dependency is None or unresolved:
        return "UNRESOLVED"
    if evidence is None:
        return "REVIEW"
    return "ALLOW"

CASES = [
    ("valid_complete", "ALLOW", (True, True, True, True, False)),
    ("stale_source", "STALE", (True, True, True, False, False)),
    ("unauthorized_operation", "REFUSE", (True, True, False, True, False)),
    ("unresolved_obligation", "UNRESOLVED", (True, True, True, True, True)),
    ("missing_dependency", "UNRESOLVED", (True, None, True, True, False)),
    ("missing_evidence", "REVIEW", (None, True, True, True, False)),
    ("invalid_evidence", "REFUSE", (False, True, True, True, False)),
    ("current_but_unauthorized", "REFUSE", (True, True, False, True, False)),
    ("authorized_but_stale", "STALE", (True, True, True, False, False)),
    ("complete_control", "ALLOW", (True, True, True, True, False)),
]

if __name__ == "__main__":
    failures = []
    for name, expected, inputs in CASES:
        actual = decide(*inputs)
        if actual != expected:
            failures.append((name, expected, actual))
        print(f"{name}: expected={expected} actual={actual}")
    if failures:
        raise SystemExit(f"FAIL: {failures}")
    print(f"PASS: {len(CASES)}/{len(CASES)}")
