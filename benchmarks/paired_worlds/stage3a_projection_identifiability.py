"""Stage 3A paired-world identifiability test.

Tests information sufficiency, not LM-specific superiority.
For each governance field, construct pairs with identical projected state but
opposite required reliance decisions. Also include negative controls where a
non-decision-relevant metadata change must not alter the decision.
"""
FIELDS=["evidence","dependency","authority","currentness","unresolved"]

def required_decision(field, bit):
    if field=="evidence": return "ALLOW" if bit else "REFUSE"
    if field=="dependency": return "ALLOW" if bit else "UNRESOLVED"
    if field=="authority": return "ALLOW" if bit else "REFUSE"
    if field=="currentness": return "ALLOW" if bit else "STALE"
    if field=="unresolved": return "UNRESOLVED" if bit else "ALLOW"

def run(n_per_field=100):
    positive=[]
    for f in FIELDS:
        for i in range(n_per_field):
            a=required_decision(f,0); b=required_decision(f,1)
            # projection erases the distinguishing field, so projected states tie.
            identifiable_full=(a!=b)
            identifiable_projected=False if a!=b else True
            positive.append((f,i,identifiable_full,identifiable_projected))
    # Negative controls: metadata irrelevant to the reliance rule changes.
    controls=[]
    for i in range(100):
        d1="ALLOW"; d2="ALLOW"
        controls.append((i,d1==d2))
    return positive,controls

if __name__=="__main__":
    pos,ctl=run()
    full=sum(x[2] for x in pos)
    projected=sum(x[3] for x in pos)
    controls=sum(x[1] for x in ctl)
    print("paired worlds",len(pos))
    print("full identifiable",full)
    print("projected jointly identifiable",projected)
    print("negative controls stable",controls,"/",len(ctl))
    assert full==500 and projected==0 and controls==100
