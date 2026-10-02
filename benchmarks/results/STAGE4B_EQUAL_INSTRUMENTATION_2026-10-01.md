# Stage 4B — Equal-Instrumentation Governed Envelope Comparator

Date: 2026-10-01  
Service: LM-AGENT-SERVICE-001 v1.0.0  
Class: **STRONG CONTROLLED COMPARATOR / NULL RESULT**

## Question

When an LM-labelled governed envelope and a conventional typed envelope receive
the same fields, update events, validation semantics and reconstruction
capability, does the frozen service decision behavior diverge?

## Equal instrumentation

Both systems received identical:
- provenance state;
- evidence state;
- dependency state;
- authority state;
- currentness/version state;
- unresolved-obligation state;
- operation scope;
- update stream;
- reconstruction events;
- decision policy.

No Sigma13 geometry, DRSC metric, LM-native label, hidden oracle or privileged
source was supplied to either side.

## Registered sequences

1. dependency omission → UNRESOLVED
2. evidence invalidation → REFUSE
3. authority retraction → REFUSE
4. operation-scope removal → REVIEW
5. stale version → STALE
6. provenance loss → UNRESOLVED
7. unresolved obligation introduced → UNRESOLVED
8. dependency reconstruction → ALLOW
9. current-version reconstruction → ALLOW
10. provenance reconstruction → ALLOW

Each sequence was evaluated immediately and after 20 neutral typed-state handoffs.

## Result

- Immediate LM expected decisions: **10/10**
- Immediate conventional expected decisions: **10/10**
- Immediate LM/conventional agreement: **10/10**
- 20-handoff LM expected decisions: **10/10**
- 20-handoff conventional expected decisions: **10/10**
- 20-handoff LM/conventional agreement: **10/10**

**Observed LM-specific decision advantage: 0 cases.**

## Disposition

**NULL for LM-specificity under explicit information and capability parity.**

The result strengthens Stage 2A and Stage 4A. A conventional typed envelope can
reproduce the same reliance behavior when it is given the same state, update
semantics and reconstruction capability.

Therefore the commercial differentiation cannot legitimately be:
- the five decision labels;
- merely carrying provenance/dependency/authority/currentness fields;
- deterministic invalidation/retraction rules;
- typed-state handoff;
- simple reconstruction after an explicitly supplied restoration event.

## Surviving question

A narrower frontier remains:

> Can LM *derive, discover, localize, or preserve* a decision-relevant relation
> that is not already explicitly supplied to both systems, under a fair
> information-equivalent source corpus and without encoding the answer in LM's
> representation?

That requires a discovery/reconstruction benchmark rather than another storage
or policy benchmark.

## Next registered test — Stage 4C

Freeze a common source corpus containing indirect dependency, provenance,
authority/currentness and unresolved-obligation evidence. Do not directly supply
the target relation. Require both systems to construct their usable dependency/
reliance state from the same corpus.

The conventional comparator must receive ordinary graph/rule traversal,
provenance propagation and dependency inference appropriate to the source data.

A favorable LM-specific result is eligible only if:
1. target relations are not pre-encoded for LM;
2. comparator receives equivalent source information and ordinary capabilities;
3. scoring is frozen before outputs;
4. LM recovers/localizes a decision-relevant state the comparator misses;
5. the difference survives inspection for representation leakage;
6. null/adverse cases remain in the ledger.
