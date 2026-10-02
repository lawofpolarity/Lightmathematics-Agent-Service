"""Stage 2 information-equivalent conventional comparator.

Deliberately contains no Sigma13, DRSC, LM metrics, geometry, or LM-native
representation. It receives the same decision-relevant fields as the frozen
LM-AGENT-SERVICE-001 contract and implements ordinary policy/rule evaluation.

If this comparator reproduces LM decisions, that result is NULL for LM-specific
decision logic and must be preserved.
"""
from dataclasses import dataclass

DECISIONS={"ALLOW","REVIEW","REFUSE","STALE","UNRESOLVED"}

@dataclass(frozen=True)
class State:
    evidence: bool|None
    dependency: bool|None
    authority: bool|None
    current: bool|None
    unresolved: bool
    operation_declared: bool=True

def conventional_policy(s: State)->str:
    if not s.operation_declared:
        return "REVIEW"
    if s.evidence is False or s.authority is False:
        return "REFUSE"
    if s.current is False:
        return "STALE"
    if s.dependency is None or s.current is None or s.authority is None or s.unresolved:
        return "UNRESOLVED"
    if s.evidence is None:
        return "REVIEW"
    return "ALLOW"

def lm_frozen_reference(s: State)->str:
    # Frozen minimal v1 contract reference. No post-comparator repair permitted.
    if not s.operation_declared:
        return "REVIEW"
    if s.evidence is False or s.authority is False:
        return "REFUSE"
    if s.current is False:
        return "STALE"
    if s.dependency is None or s.current is None or s.authority is None or s.unresolved:
        return "UNRESOLVED"
    if s.evidence is None:
        return "REVIEW"
    return "ALLOW"

def exhaustive_cases():
    vals=[True,False,None]
    for e in vals:
      for d in vals:
       for a in vals:
        for c in vals:
         for u in [False,True]:
          for op in [True,False]:
           yield State(e,d,a,c,u,op)

if __name__=="__main__":
    cases=list(exhaustive_cases())
    mismatches=[]
    counts={d:0 for d in DECISIONS}
    for s in cases:
        lm=lm_frozen_reference(s)
        cv=conventional_policy(s)
        counts[lm]+=1
        if lm!=cv: mismatches.append((s,lm,cv))
    print("cases",len(cases))
    print("LM decisions",counts)
    print("mismatches",len(mismatches))
    if mismatches:
        for x in mismatches[:20]: print(x)
        raise SystemExit(1)
    print("NULL: conventional policy reproduces frozen minimal decision logic under information parity")
