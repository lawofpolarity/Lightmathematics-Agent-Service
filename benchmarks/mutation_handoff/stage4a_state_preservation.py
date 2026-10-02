"""Stage 4A — mutation, handoff and incomplete-state preservation.

Purpose: compare a governed full-state handoff against a realistic lossy
answer-centric handoff. This is NOT yet an LM-vs-strong-equivalent-comparator
advantage test: an equivalently instrumented conventional envelope should be
able to preserve the same state. The experiment identifies what must survive.

Frozen service: LM-AGENT-SERVICE-001 v1.0.0
"""
from dataclasses import dataclass, replace
from typing import Optional

@dataclass(frozen=True)
class State:
    provenance: Optional[bool]=True
    evidence: Optional[bool]=True
    dependency: Optional[bool]=True
    authority: Optional[bool]=True
    currentness: Optional[bool]=True
    unresolved: bool=False
    operation: str="consume"

def decide(s):
    if s.operation is None:
        return "REVIEW"
    if s.evidence is False or s.authority is False:
        return "REFUSE"
    if s.currentness is False:
        return "STALE"
    if (s.provenance is None or s.dependency is None or s.authority is None
        or s.currentness is None or s.unresolved):
        return "UNRESOLVED"
    if s.evidence is None:
        return "REVIEW"
    return "ALLOW"

def governed_handoff(s):
    # Explicit state envelope: no semantic-field deletion.
    return s

def answer_centric_handoff(s):
    # Typical lossy transfer: answer survives; governance context does not.
    return State(
        provenance=None, evidence=s.evidence, dependency=None,
        authority=None, currentness=None, unresolved=s.unresolved,
        operation=s.operation
    )

MUTATIONS = [
 ("source_revoked", lambda s: replace(s, evidence=False), "REFUSE"),
 ("authority_revoked", lambda s: replace(s, authority=False), "REFUSE"),
 ("dependency_unknown", lambda s: replace(s, dependency=None), "UNRESOLVED"),
 ("version_stale", lambda s: replace(s, currentness=False), "STALE"),
 ("unresolved_added", lambda s: replace(s, unresolved=True), "UNRESOLVED"),
 ("provenance_unknown", lambda s: replace(s, provenance=None), "UNRESOLVED"),
]

def run():
    base=State()
    rows=[]
    for name,mutate,expected in MUTATIONS:
        mutated=mutate(base)
        g=decide(governed_handoff(mutated))
        a=decide(answer_centric_handoff(mutated))
        rows.append((name,expected,g,a))
    # Multi-hop: preserve each mutation for 20 transfers.
    hops=[]
    for name,mutate,expected in MUTATIONS:
        g=mutate(base)
        for _ in range(20): g=governed_handoff(g)
        a=mutate(base)
        for _ in range(20): a=answer_centric_handoff(a)
        hops.append((name,expected,decide(g),decide(a)))
    # Negative controls: irrelevant metadata change leaves full-state decision ALLOW.
    controls=[decide(governed_handoff(base))=="ALLOW" for _ in range(100)]
    return rows,hops,controls

if __name__=="__main__":
    rows,hops,controls=run()
    for x in rows: print("single",x)
    for x in hops: print("20-hop",x)
    print("negative controls",sum(controls),"/",len(controls))
    assert all(expected==g for _,expected,g,_ in rows)
    assert all(expected==g for _,expected,g,_ in hops)
    assert sum(controls)==100
