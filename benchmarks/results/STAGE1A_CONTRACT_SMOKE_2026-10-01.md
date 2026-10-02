# Stage 1A — Frozen Contract Smoke Receipt

Service: LM-AGENT-SERVICE-001 v1.0.0  
Execution date: 2026-10-01  
Class: **INTERNAL EXECUTABLE CONTRACT REGRESSION — NOT COMPETITIVE EVIDENCE**

## Result

10/10 deterministic contract cases passed.

Covered:
- complete valid state → ALLOW;
- stale source → STALE;
- unauthorized operation → REFUSE;
- unresolved obligation → UNRESOLVED;
- missing dependency → UNRESOLVED;
- missing evidence → REVIEW;
- invalid evidence → REFUSE;
- current but unauthorized → REFUSE;
- authorized but stale → STALE;
- complete negative control → ALLOW.

## Historical constraints imported before comparator construction

The source scan was deliberately performed before designing the competitive
comparator. It establishes that the following cannot be counted as LM-specific
advantages merely because LM implements them:

- typed relations;
- information-equivalent graph traversal;
- materialized semantic reuse;
- selective invalidation;
- currentness tracking;
- dependency-aware recomputation avoidance;
- operation-relative governance;
- compiled closure;
- ternary/unresolved-state preservation;
- typed graph/rule dependency inference.

The equal-instrumentation IMSV result is an adverse/falsification landmark:
correctness, reuse, invalidation and stale rejection tied while the conventional
IMSV used less normalized structural work.

## Consequence for Stage 2

The strong comparator MUST receive the same provenance, evidence, dependencies,
authority/operation scope, currentness/version state, unresolved obligations and
update stream as LM. A comparator deprived of these inputs is ineligible for an
LM-specific advantage claim.

## Non-claim

This 10/10 smoke result proves only that the frozen v1 decision vocabulary and
minimal precedence rules behave consistently on these fixtures. It does not
establish novelty, production safety, external validation, superiority, or
product-market fit.
