# Stage 2A — Information-Equivalent Conventional Policy Comparator

Date: 2026-10-01  
Service: LM-AGENT-SERVICE-001 v1.0.0  
Class: **CONTROLLED INTERNAL COMPARATOR / NULL RESULT**

## Predeclared question

Does the frozen minimal LM reliance decision logic itself require an LM-specific
mechanism when a conventional policy/rule implementation receives the same
decision-relevant information?

## Comparator

A conventional deterministic policy evaluator was implemented without Sigma13,
DRSC, LM-native metrics, geometry, or LM-specific representation.

It received the same fields:
- evidence state;
- dependency state;
- authority state;
- currentness state;
- unresolved-obligation state;
- declared-operation presence.

The LM frozen reference and conventional policy were evaluated over the complete
Cartesian state fixture used by this minimal model:

3 evidence states × 3 dependency states × 3 authority states × 3 currentness
states × 2 unresolved states × 2 operation-declared states = **324 cases**.

## Result

**324/324 decisions matched. Mismatches: 0.**

Frozen-reference decision distribution:
- REVIEW: 164
- REFUSE: 90
- UNRESOLVED: 44
- STALE: 24
- ALLOW: 2

## Disposition

**NULL for LM-specificity of the minimal decision rule.**

A conventional rule/policy engine supplied with information-equivalent state can
reproduce the frozen minimal ALLOW/REVIEW/REFUSE/STALE/UNRESOLVED mapping exactly.

This result is constitutionally important: the product cannot claim that the
five-state decision vocabulary or elementary precedence rules are themselves a
LightMathematics-specific computational advantage.

## What remains open

The commercially/research-relevant question narrows to whether LM supplies,
maintains, resolves, or preserves the *decision-relevant state* better across
real transformations and incomplete/mutating systems, or produces superior
evidence receipts/integration economics under fair information parity.

That requires Stage 2B/3 tests of:
- dependency discovery and omission;
- evidence/provenance continuity;
- authority changes;
- currentness/version transitions;
- unresolved-obligation preservation;
- projection/representation loss;
- selective retraction/re-derivation;
- evidence receipt completeness;
- adversarial paired worlds and negative controls.

## Non-claims

This test does not establish external equivalence to LangSmith, Glean, Phoenix,
Patronus, TMS/ATMS, Datalog/provenance systems, or production policy engines.
It establishes only that an ordinary conventional policy implementation can
reproduce the frozen minimal decision function when given the same state.

The null result is permanent evidence and must remain visible if later tests are
favorable.
