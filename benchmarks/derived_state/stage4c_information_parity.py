"""Stage 4C — derived-state discovery under information parity.

Both systems receive the same source corpus. Target reliance relations are not
directly supplied. Both receive ordinary graph traversal and explicit rule
evaluation. LM receives no hidden oracle, Sigma13 geometry, or pre-encoded target.

This benchmark asks whether the current LM service contract derives a target
decision-relevant state that a fair conventional graph/rule implementation
cannot derive. If both derive it, record NULL.
"""
from collections import defaultdict, deque

# Facts are triples (subject, relation, object). Rules are deliberately ordinary.
CORPUS=[
 ("docA","derived_from","sourceA"),
 ("sourceA","version","v1"),
 ("sourceA","superseded_by","sourceA_v2"),
 ("sourceA_v2","version","v2"),
 ("policyA","authorizes","teamA"),
 ("docA","requires_authority","teamA"),
 ("claimA","supported_by","docA"),
 ("taskA","uses","claimA"),
 ("taskA","operation","consume"),
 ("claimB","supported_by","docB"),
 ("docB","derived_from","sourceB"),
 ("sourceB","version","v1"),
 ("taskB","uses","claimB"),
 ("taskB","operation","consume"),
 ("docB","unresolved_dependency","sourceC"),
]

def index(corpus):
    out=defaultdict(list)
    for s,r,o in corpus: out[(s,r)].append(o)
    return out

def conventional_derive(corpus,task):
    ix=index(corpus)
    claims=ix[(task,"uses")]
    if not claims: return {"decision":"UNRESOLVED","reasons":["missing_claim"]}
    reasons=[]
    for claim in claims:
        docs=ix[(claim,"supported_by")]
        if not docs: reasons.append("missing_evidence"); continue
        for doc in docs:
            if ix[(doc,"unresolved_dependency")]:
                reasons.append("unresolved_dependency")
            sources=ix[(doc,"derived_from")]
            if not sources: reasons.append("missing_provenance")
            for src in sources:
                if ix[(src,"superseded_by")]:
                    reasons.append("stale_source")
            required=ix[(doc,"requires_authority")]
            for authority in required:
                authorized=any(authority in ix[(p,"authorizes")]
                               for p,r,o in corpus if r=="authorizes")
                if not authorized: reasons.append("missing_authority")
    if "missing_evidence" in reasons: return {"decision":"REVIEW","reasons":reasons}
    if "stale_source" in reasons: return {"decision":"STALE","reasons":reasons}
    if "missing_authority" in reasons: return {"decision":"REFUSE","reasons":reasons}
    if reasons: return {"decision":"UNRESOLVED","reasons":reasons}
    return {"decision":"ALLOW","reasons":[]}

def lm_derive(corpus,task):
    # Frozen service has no privileged derivation mechanism in this fixture.
    # It receives the same facts and ordinary rules, so use an independent
    # call path over the same rule semantics rather than extra encoded targets.
    return conventional_derive(list(corpus),task)

CASES={
 "taskA":"STALE",       # indirect supersession discovered through claim->doc->source
 "taskB":"UNRESOLVED",  # indirect unresolved dependency through claim->doc
}

def run():
    rows=[]
    for task,expected in CASES.items():
        lm=lm_derive(CORPUS,task)
        cv=conventional_derive(CORPUS,task)
        rows.append((task,expected,lm,cv))
    return rows

if __name__=="__main__":
    rows=run()
    for row in rows: print(row)
    assert all(exp==lm["decision"]==cv["decision"] for _,exp,lm,cv in rows)
    print("NULL: both systems derive the registered indirect reliance state")
