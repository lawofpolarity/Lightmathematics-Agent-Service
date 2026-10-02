"""Stage 4B — equal-instrumentation governed envelope comparison.

LM-labelled and conventional envelopes receive identical fields, update events,
validation rules and reconstruction capability. This test is designed to detect
whether any observed advantage survives information/capability parity.

No LM geometry, Sigma13, DRSC metric, or hidden oracle is supplied.
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
    operation_scope: str="consume"

def decide(s):
    if not s.operation_scope: return "REVIEW"
    if s.evidence is False or s.authority is False: return "REFUSE"
    if s.currentness is False: return "STALE"
    if s.provenance is None or s.dependency is None or s.authority is None or s.currentness is None or s.unresolved:
        return "UNRESOLVED"
    if s.evidence is None: return "REVIEW"
    return "ALLOW"

# Both systems intentionally use the same explicit update semantics.
def apply_event(s,event):
    kind=event[0]
    if kind=="omit_dependency": return replace(s,dependency=None)
    if kind=="invalidate_evidence": return replace(s,evidence=False)
    if kind=="retract_authority": return replace(s,authority=False)
    if kind=="scope_change": return replace(s,operation_scope=event[1])
    if kind=="stale_version": return replace(s,currentness=False)
    if kind=="lose_provenance": return replace(s,provenance=None)
    if kind=="add_unresolved": return replace(s,unresolved=True)
    if kind=="restore_dependency": return replace(s,dependency=True)
    if kind=="restore_current": return replace(s,currentness=True)
    if kind=="restore_provenance": return replace(s,provenance=True)
    raise ValueError(kind)

class LMEnvelope:
    def __init__(self,s): self.state=s
    def event(self,e): self.state=apply_event(self.state,e)
    def decision(self): return decide(self.state)

class ConventionalTypedEnvelope:
    def __init__(self,s): self.state=s
    def event(self,e): self.state=apply_event(self.state,e)
    def decision(self): return decide(self.state)

SEQUENCES=[
 ("dependency_omission",[("omit_dependency",)],"UNRESOLVED"),
 ("evidence_invalidation",[("invalidate_evidence",)],"REFUSE"),
 ("authority_retraction",[("retract_authority",)],"REFUSE"),
 ("scope_removal",[("scope_change","")],"REVIEW"),
 ("stale_version",[("stale_version",)],"STALE"),
 ("provenance_loss",[("lose_provenance",)],"UNRESOLVED"),
 ("unresolved_added",[("add_unresolved",)],"UNRESOLVED"),
 ("dependency_reconstruction",[("omit_dependency",),("restore_dependency",)],"ALLOW"),
 ("version_reconstruction",[("stale_version",),("restore_current",)],"ALLOW"),
 ("provenance_reconstruction",[("lose_provenance",),("restore_provenance",)],"ALLOW"),
]

def run():
    rows=[]
    for name,events,expected in SEQUENCES:
        lm=LMEnvelope(State()); cv=ConventionalTypedEnvelope(State())
        for e in events: lm.event(e); cv.event(e)
        rows.append((name,expected,lm.decision(),cv.decision()))
    # Repeat each sequence through 20 neutral handoffs preserving the same typed state.
    hops=[]
    for name,events,expected in SEQUENCES:
        lm=LMEnvelope(State()); cv=ConventionalTypedEnvelope(State())
        for e in events: lm.event(e); cv.event(e)
        for _ in range(20):
            lm=LMEnvelope(lm.state); cv=ConventionalTypedEnvelope(cv.state)
        hops.append((name,expected,lm.decision(),cv.decision()))
    return rows,hops

if __name__=="__main__":
    rows,hops=run()
    for x in rows: print("single",x)
    for x in hops: print("20-hop",x)
    assert all(exp==lm==cv for _,exp,lm,cv in rows)
    assert all(exp==lm==cv for _,exp,lm,cv in hops)
    print("NULL: equal instrumentation produces equal decisions on all registered sequences")
