# LM-AGENT-SERVICE-001 v1.0.0

Status: **FROZEN EXPERIMENTAL CONTRACT — PRE-EXTERNAL-COHORT**

## Purpose
Given an information object/claim and a declared intended operation, inspect the
decision-relevant state needed to determine whether reliance is presently justified.

## Frozen pipeline
```text
Request → Evidence Lookup → Provenance → Dependencies → Authority → Currentness
→ Unresolved Obligations → Reliance Decision → Evidence Receipt
```

## Decisions
`ALLOW | REVIEW | REFUSE | STALE | UNRESOLVED`

## Required inputs
Where available: provenance, evidence, dependencies, authority/operation scope,
currentness/version state, unresolved obligations, and declared intended operation.
Missing state remains explicit. Absence is neither automatically failure nor permission.

## Output
A completed inspection records decision, operation, inspected object/reference,
available provenance/evidence/dependencies, authority/currentness, unresolved
obligations, source versions, reliance scope, limitations, service version,
pricing version where applicable, and receipt identifier.

## Economic invariant
Payment status is not a semantic input:
`payment authorization != semantic authority`.
Paid does not mean true, verified, canonical, admitted, or favorable.

## Contribution invariant
```text
Agent observation → contribution envelope → quarantine → validation
→ duplicate/conflict check → benchmark/review → candidate
→ separately authorized admission
```
No automatic agent-to-canon transition exists.

## Benchmark freeze
v1.0.0 is evaluated without post-result semantic modification against:
1. historical LM positive results;
2. historical null/adverse/falsification results;
3. an information-equivalent conventional implementation;
4. paired-world/ablation cases;
5. negative controls where removed information should not change the decision;
6. later, genuinely independent external-agent use.

Comparators receive equal information and instrumentation. Preserve losses,
equivalences, nulls, and favorable results.

## Claim boundary
This contract is a product and experimental hypothesis. It does not itself
establish literature-level novelty, LM-specific computational superiority,
Sigma13 privilege, production safety, or product-market fit.

## Change rule
Any semantic change to inputs, decisions, decision rules, receipt semantics,
benchmark eligibility, or scoring after testing begins requires a new version.
Historical v1.0.0 results remain immutable.
