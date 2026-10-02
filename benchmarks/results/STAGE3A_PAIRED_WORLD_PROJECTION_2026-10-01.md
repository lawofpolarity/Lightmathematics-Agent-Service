# Stage 3A — Paired-World Projection Identifiability

Date: 2026-10-01  
Service: LM-AGENT-SERVICE-001 v1.0.0  
Class: **FORMAL/CONTROLLED INFORMATION-SUFFICIENCY RESULT — NOT LM-SPECIFIC**

## Design

Five decision-relevant field families were tested:
evidence, dependency, authority, currentness, unresolved obligation.

For each family, 100 paired worlds were constructed in which the underlying
field state requires opposite reliance decisions while the projected
representation erases that distinguishing field.

Total: **500 paired worlds**.

A separate set of 100 negative controls changed metadata that is irrelevant to
the frozen reliance rule; the correct reliance decision was required to remain
unchanged.

## Result

- Full state decision-identifiable: **500/500**
- Field-ablated projected pairs jointly identifiable: **0/500**
- Negative controls preserving decision: **100/100**

## Interpretation

The result extends the prior projection-loss principle across the five service
field families used here: when projection collapses states that require different
correct decisions, no decision function operating only on the collapsed
projection can uniquely recover the missing distinction.

The negative controls matter: not every information difference is
decision-relevant. A system should not refuse merely because *something* changed.

## Disposition

**POSITIVE information-sufficiency result; NOT an LM-specific advantage.**

This test establishes why the service must preserve or recover decision-relevant
state. It does not establish that LM preserves/reconstructs that state better
than an information-equivalent conventional system.

Stage 2A already showed that once equivalent state is available, ordinary policy
logic reproduces the frozen five-state decision rule exactly.

Therefore the surviving differentiation question is upstream of the elementary
decision mapping: whether the LM architecture can maintain, discover, validate,
or transfer the required state under mutation, projection, handoff and
incomplete knowledge more effectively, with useful evidence receipts and
competitive cost.

## Permanent paired finding

Taken together:

1. **Stage 2A:** information-equivalent conventional policy = LM frozen decision
   mapping on 324/324 minimal states (NULL for LM-specific decision logic).
2. **Stage 3A:** erase a decision-relevant distinction and the correct decision
   becomes non-identifiable from the projection (500/500 → 0/500), while
   irrelevant changes leave decisions stable (100/100).

The commercial experiment must therefore test preservation/resolution of
decision-relevant state, not merely whether LM can emit ALLOW/REFUSE labels.
