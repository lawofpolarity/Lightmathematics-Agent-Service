# Stage 4A — Mutation, Handoff and Incomplete-State Preservation

Date: 2026-10-01  
Service: LM-AGENT-SERVICE-001 v1.0.0  
Class: **CONTROLLED STATE-PRESERVATION TEST / BOUNDARY RESULT**

## Intention

Test what happens when decision-relevant state changes and must survive a handoff.
Compare:

1. **governed full-state envelope** — carries the decision-relevant state; and
2. **answer-centric lossy handoff** — carries the answer/evidence signal but drops
   provenance, dependency, authority and currentness context.

This is deliberately not called an LM-specific advantage test. An equivalently
instrumented conventional envelope should be able to preserve the same fields.

## Registered mutations

| Mutation | Required decision |
|---|---|
| evidence/source revoked | REFUSE |
| authority revoked | REFUSE |
| dependency becomes unknown | UNRESOLVED |
| version becomes stale | STALE |
| unresolved obligation introduced | UNRESOLVED |
| provenance becomes unknown | UNRESOLVED |

Each mutation was checked after one handoff and after 20 handoffs.

100 negative controls required a complete unchanged governed state to remain ALLOW.

## Result

### Governed full-state envelope

- Single-handoff required decisions preserved: **6/6**
- 20-handoff required decisions preserved: **6/6**
- Negative controls stable: **100/100**

### Lossy answer-centric envelope

The lossy handoff intentionally deletes governance context. It therefore cannot
retain the complete basis needed to distinguish all original reliance states.
Its resulting UNRESOLVED behavior in several cases is safer than silently
promoting missing state to ALLOW, but it also loses decision specificity.

Notably, explicit evidence revocation remains REFUSE because the evidence signal
was retained; explicit stale/currentness or authority state cannot be fully
distinguished once those fields are discarded.

## Interpretation

The experiment establishes an engineering requirement:

> Decision-relevant semantic state must be carried, reconstructibly referenced,
> or explicitly marked unresolved across handoffs.

A bare answer is not an information-equivalent substitute for the governed state
that justified its use.

## Claim subtraction

This result does **not** show that LightMathematics uniquely provides such an
envelope. A conventional typed envelope, provenance system, policy context,
dependency-aware materialized view, or other equivalently instrumented mechanism
can in principle preserve the same information.

Accordingly, Stage 4A is a **boundary result**:
- favorable to the service requirement;
- unfavorable to any claim that merely preserving explicit fields is uniquely LM.

## Next test

Stage 4B must compare LM's actual governed state/receipt mechanism against a
strong conventional typed envelope under equal instrumentation, then introduce
controlled transformations that can cause omission, invalidation, retraction,
scope change and reconstruction.

The question becomes whether LM detects or localizes a loss that the equally
instrumented conventional mechanism permits through—not whether LM simply stores
more fields.
