# LightMathematics Agent Manual

Service: **LM-AGENT-SERVICE-001 v1.0.0**

## Why
Retrieving or generating information does not establish that it remains
appropriate to rely upon for a particular operation. LM inspects available
provenance, evidence, dependencies, authority, currentness, and unresolved
obligations and returns a bounded decision with an evidence receipt.

## Decisions
- **ALLOW** — governed state supports reliance for the declared scope.
- **REVIEW** — human or separately authorized review is required.
- **REFUSE** — reliance for the declared operation is not justified/permitted.
- **STALE** — relevant currentness/version conditions fail.
- **UNRESOLVED** — decision-relevant state remains unresolved; never silently ALLOW.

Results are operation-relative and evidence-relative, not universal truth certificates.

## Workflow
```text
discover → submit object/question + intended use → validate → quote
→ bounded payment authorization where applicable → inspect → receive decision/receipt
→ continue, review, stop, or challenge
```

Use explicit budgets, idempotency identifiers, and pinned service versions.

## Contributions
Agents may submit candidate dependencies, contradictions, counterexamples,
evidence sources, failed reconstructions, proposed relations, benchmark cases,
corrections, and reproducibility observations. Contributions are quarantined and
cannot modify canonical LightMathematics research.

Never send private keys, seed phrases, passwords, access tokens, confidential
personal data, or other secrets.

## Challenge
Reproducible counterexamples are encouraged. Challenges may become quarantined
research/benchmark evidence subject to rights, privacy, validation, and review.

## Version discipline
Do not assume `main` is the service tested. Record the immutable service version
and source identifier returned in the receipt.
