# LightMathematics Agent Service

**Governed reliance inspection for AI agents — evaluating provenance, evidence, dependencies, authority, currentness, and unresolved obligations before information is used.**

## LM-AGENT-SERVICE-001

The frozen experimental service contract asks a bounded question:

> Given this information and this intended operation, is reliance presently justified?

```text
Agent request
→ capability discovery
→ object/question + intended use
→ validation
→ quote/payment authorization where applicable
→ governed inspection
→ ALLOW | REVIEW | REFUSE | STALE | UNRESOLVED
→ evidence receipt
```

The service evaluates available **provenance, evidence, dependencies, authority, currentness, unresolved obligations, and intended-use scope**.

## Experimental status

**v1.0.0 is a frozen pre-external-cohort contract.** This repository does not claim LightMathematics is superior to existing evaluation, provenance, governance, observability, or dependency-aware systems. The benchmark program tests that proposition prospectively against strong information-equivalent comparators and preserves positive, null, equivalent, falsifying, and adverse results.

Payment purchases declared computation/service only. It does **not** purchase truth, verification, certification, canonical status, authority, admission, or a favorable decision.

## Authority boundary

This is an agent-facing service repository, **not the canonical LightMathematics research corpus**. It has no authority to admit or rewrite canonical research.

Agent contributions follow:

```text
observation → contribution envelope → quarantine → validation
→ duplicate/conflict checks → benchmark/review → candidate
→ separately authorized admission
```

Never: `agent → canonical GitHub`.

## Version pinning

Production sites and clients must not treat mutable `main` as authority. Deployments must pin an immutable tested release/tag or commit SHA.

## Repository map

- `specification/` — frozen normative service contract
- `schemas/` — machine-readable contracts
- `pricing/` — versioned pricing policy
- `benchmarks/` — prospective test program and results
- `AGENTS.md` — agent/developer manual
- `NOTICE` — scope and attribution

## Security

No external agent or browser receives credentials capable of modifying canonical LightMathematics repositories. Never commit wallet private keys, seed phrases, signing secrets, or privileged GitHub credentials.

Production x402 settlement remains disabled until an exact public receiver address, network, asset, purpose, and verification state are explicitly verified.

## License

Software and documentation are licensed under Apache License 2.0 unless a file states otherwise. Canonical LightMathematics research authority, trademarks, private datasets, credentials, hosted-service access, and third-party rights are not granted merely by repository inclusion.

Copyright 2026 Bernard Yankson / LightMathematics.
