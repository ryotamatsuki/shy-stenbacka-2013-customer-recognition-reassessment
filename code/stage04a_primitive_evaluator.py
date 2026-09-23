from __future__ import annotations
import math
import numpy as np
from scipy.optimize import differential_evolution

SQ3=math.sqrt(3.0)
ZC=(-6+4*SQ3)/3
TYPES=(('HH',0.0),('HL',1.0),('LH',-1.0),('LL',0.0))

def clipped_switch_mass(x: float)->float:
    return max(0.0,min(1.0,x))

def primitive_segment_incumbent_profit(p: float,q: float,z: float)->float:
    ans=0.0
    for _,sgn in TYPES:
        d=z*sgn
        s=clipped_switch_mass(p-q-d)
        ans += p*(1.0-s)
    return ans

def primitive_segment_poacher_profit(q: float,p: float,z: float)->float:
    ans=0.0
    for _,sgn in TYPES:
        d=z*sgn
        s=clipped_switch_mass(p-q-d)
        ans += q*s
    return ans

def argmax_1d(fun, hi=2.0):
    res=differential_evolution(lambda X:-fun(float(X[0])),[(0.0,hi)],seed=20260923,tol=1e-12,polish=True)
    return float(res.x[0]), float(-res.fun)

def source_profile_test(z: float):
    p=2/3; q=1/3
    pbr,pv=argmax_1d(lambda x:primitive_segment_incumbent_profit(x,q,z))
    qbr,qv=argmax_1d(lambda x:primitive_segment_poacher_profit(x,p,z))
    return {
      'z':z,'p':p,'q':q,'p_br':pbr,'q_br':qbr,
      'p_gain':pv-primitive_segment_incumbent_profit(p,q,z),
      'q_gain':qv-primitive_segment_poacher_profit(q,p,z)
    }

def mixed_candidate(z:float):
    p=z*(3+2*SQ3)/3
    qL=p/2
    qH=z*(2+SQ3)/3
    lam=(4-(5+3*SQ3)*z)/(z*(1+SQ3))
    return p,qL,qH,lam

def mixed_test(z:float):
    p,qL,qH,lam=mixed_candidate(z)
    qbr,qv=argmax_1d(lambda q:primitive_segment_poacher_profit(q,p,z))
    qeq=primitive_segment_poacher_profit(qL,p,z)
    qeq2=primitive_segment_poacher_profit(qH,p,z)
    def EU(pp):
        return lam*primitive_segment_incumbent_profit(pp,qL,z)+(1-lam)*primitive_segment_incumbent_profit(pp,qH,z)
    pbr,pv=argmax_1d(EU)
    peq=EU(p)
    return {
      'z':z,'p':p,'qL':qL,'qH':qH,'lambda':lam,
      'p_br':pbr,'p_gain':pv-peq,
      'q_br_one_maximizer':qbr,'q_gain':qv-qeq,'q_support_gap':qeq2-qeq
    }

def exact_counterexample_numeric():
    sig=25.0; Delta=8.0; z=Delta/sig
    p=2*sig/3; q0=sig/3; q1=29/3
    base=sig*primitive_segment_poacher_profit(q0/sig,p/sig,z)
    dev=sig*primitive_segment_poacher_profit(q1/sig,p/sig,z)
    return base,dev,dev-base

def run():
    rows=[]
    for z in [0.01,0.05,0.10,0.20,0.28,0.30,ZC-1e-6,ZC,ZC+1e-6,0.31,0.32,1/3-1e-6]:
        rows.append(source_profile_test(z))
    mixed=[]
    for z in [ZC+1e-5,0.31,0.32,0.33,1/3-1e-5]:
        mixed.append(mixed_test(z))
    base,dev,gain=exact_counterexample_numeric()
    assert abs(gain-23/225)<1e-9
    assert max(r['q_gain'] for r in rows if r['z']<ZC-1e-7) < 1e-8
    assert min(r['q_gain'] for r in rows if r['z']>ZC+1e-7) > 0
    assert max(abs(r['p_gain']) for r in mixed) < 1e-8
    assert max(abs(r['q_gain']) for r in mixed) < 1e-8
    assert max(abs(r['q_support_gap']) for r in mixed) < 1e-8
    print('primitive_evaluator=PASS')
    print('exact_counterexample',base,dev,gain)
    print('source_rows')
    for r in rows: print(r)
    print('mixed_rows')
    for r in mixed: print(r)

if __name__=='__main__':
    run()
