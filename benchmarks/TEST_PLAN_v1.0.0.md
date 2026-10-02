# LM-AGENT-SERVICE-001 — Frozen Test Plan v1.0.0

Status: **FROZEN BASELINE / PRE-EXTERNAL-COHORT**  
Date: 2026-10-01

## Intention

Determine whether an independent agent, developer, or organization has a reason
to purchase a LightMathematics governed reliance inspection because it preserves,
discovers, validates, or transfers decision-relevant semantic state that would
otherwise be lost or mishandled.

The program is designed to falsify as well as support that proposition.

## Primary product question

> Given an information object and a declared intended operation, can the service
> identify a decision-relevant reason to allow, review, refuse, mark stale, or
> leave unresolved reliance, while preserving enough evidence to explain the
> decision?

## Differentiation question

The five-state decision vocabulary is not presumed novel. The tested
differentiation is whether the complete system preserves/resolves
decision-relevant state across mutation, projection, handoff and incomplete
knowledge better than strong information- and capability-equivalent conventional
systems at competitive cost.

## Frozen decision vocabulary

ALLOW | REVIEW | REFUSE | STALE | UNRESOLVED

## Decision-relevant fields

- P: provenance
- E: evidence
- D: dependencies
- A: authority and operation scope
- C: currentness/version state
- U: unresolved obligations
- O: declared intended operation

## Test stages

### Stage 1 — Historical regression
Import positive, null, adverse, failure-condition and falsification results from
the existing LM research record. Verify that the service contract does not erase
earlier losses.

### Stage 2 — Strong conventional comparator
Give a conventional policy/rule implementation the same decision-relevant state.
Then progressively strengthen the comparator toward TMS/ATMS, provenance/rule
systems and incremental materialized views where appropriate.

### Stage 3 — Paired worlds and ablations
Construct states requiring different correct decisions, project away one
decision-relevant distinction, and test identifiability. Include controls where
information changes but the correct decision must remain unchanged.

### Stage 4 — Mutation / handoff / incomplete state
Test whether required state survives:
- source/version mutation;
- dependency mutation and omission;
- authority revocation/scope change;
- stale-to-current and current-to-stale transition;
- unresolved obligation across transformation;
- evidence/provenance handoff;
- selective retraction/re-derivation;
- summarization/projection.

### Stage 5 — External-agent cohort
After sandbox deployment and immutable release pinning, invite genuinely
independent agents/developers. Do not alter v1.0.0 based on their performance.

## Comparator fairness

A comparator must receive the same legitimate source facts, evidence,
dependencies, provenance, authority, operation scope, version/currentness,
negative/frontier dependencies, unresolved state, update stream and ordinary
inference capabilities relevant to the claim.

Withholding equivalent information invalidates an LM-specific advantage claim.

## Required measurements

- eligible cases;
- correct decision;
- false ALLOW;
- false REFUSE;
- REVIEW/UNRESOLVED calibration;
- comparator agreement/disagreement;
- decision-relevant state retained/lost;
- evidence receipt completeness;
- normalized structural work where meaningful;
- latency and actual cost when production measurement exists;
- external repeat use;
- inspections purchased;
- contribution rate;
- accepted useful contributions;
- Corrective Action Rate (CAR);
- Reliance Integrity Rate (RIR), where applicable.

## CAR

CAR = demonstrably correct downstream action changes caused by LM /
      eligible completed external inspections

CAR is an external-product metric. Synthetic fixtures must not be reported as
commercial CAR.

## Stop / narrowing rules

- Comparator reproduces effect under information parity → subtract mechanism
  from LM-specific explanation.
- Missing dependency defeats both systems → record failure condition.
- LM loses → preserve adverse result.
- Result depends on cheaper comparator reconstruction → report cost frontier.
- Geometry/LM labels are not causal evidence without ablation.
- Post-result rule repair requires a new service/benchmark version.

## Claim boundary

Internal synthetic tests establish controlled behavior only. They do not establish
production performance, external validation, product-market fit, literature-level
novelty, or superiority over named commercial products.
