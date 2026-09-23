from __future__ import annotations
import math
from scipy.integrate import quad
from scipy.optimize import brentq

SQ3=math.sqrt(3.0)
ZC=(-6+4*SQ3)/3.0

def clip(x:float)->float:
    return max(0.0,min(1.0,x))

def mixed(z:float):
    p=z*(3+2*SQ3)/3
    qL=p/2
    qH=z*(2+SQ3)/3
    lam=(4-(5+3*SQ3)*z)/(z*(1+SQ3))
    return p,qL,qH,lam

def types(z:float,L:float):
    return [
      ("HH",L+z,L+z),
      ("HL",L+z,L),
      ("LH",L,L+z),
      ("LL",L,L),
    ]

def consumer_surplus_base(p_by_type,q_by_type,z:float,L:float):
    total=0.0
    for t,vA,vB in types(z,L):
        p=p_by_type[t] if isinstance(p_by_type,dict) else p_by_type
        q=q_by_type[t] if isinstance(q_by_type,dict) else q_by_type
        total += quad(lambda s:max(vA-p,vB-q-s),0.0,1.0,epsabs=1e-11,epsrel=1e-11)[0]
    return total

def switching_mass(p:float,q:float,d:float)->float:
    return clip(p-q-d)

def cs_mixed(z:float,L:float):
    p,qL,qH,lam=mixed(z)
    return lam*consumer_surplus_base(p,qL,z,L)+(1-lam)*consumer_surplus_base(p,qH,z,L)

def cs_share(z:float,L:float):
    p={"HH":2/3,"HL":(2+z)/3,"LH":(2-z)/3,"LL":2/3}
    q={"HH":1/3,"HL":(1-z)/3,"LH":(1+z)/3,"LL":1/3}
    return consumer_surplus_base(p,q,z,L)

def cs_noshare(z:float,L:float):
    p={"HH":2/3,"HL":2/3+z/2,"LH":2/3-z/2,"LL":2/3}
    return consumer_surplus_base(p,1/3,z,L)

def f_cs_mixed(z,L):
    return (24*L+z*z-20*z-8*SQ3*z)/6

def f_cs_share(z,L):
    return (z*z+18*(2*L+z)-22)/9

def f_cs_noshare(z,L):
    return (9*z*z+72*(2*L+z)-88)/36

def profit_mixed(z):
    return z*((2+SQ3)*z+10+6*SQ3)/3

def profit_share(z):
    return 4*(z*z+5)/9

def profit_noshare(z):
    return (9*z*z+40)/18

def switching_counts_mixed(z):
    p,qL,qH,lam=mixed(z)
    xL=p-qL
    xH=p-qH
    TI=2*(lam*clip(xL-z)+(1-lam)*clip(xH-z))
    TE=2*(lam*clip(xL+z)+(1-lam)*clip(xH+z))
    return TI,TE

def switching_counts_share(z):
    return 2*(1-z)/3, 2*(1+z)/3

def switching_counts_noshare(z):
    return (2-3*z)/3, (2+3*z)/3

def total_welfare(cs,profit,k=0.0):
    return 2*cs+2*profit-2*k

def run():
    L=2.0
    grid=[ZC+1e-5,0.31,0.315,0.32,0.325,0.33,1/3-1e-5]
    for z in grid:
        cm=cs_mixed(z,L)
        cs=cs_share(z,L)
        cn=cs_noshare(z,L)
        assert abs(cm-f_cs_mixed(z,L))<5e-9
        assert abs(cs-f_cs_share(z,L))<5e-9
        assert abs(cn-f_cs_noshare(z,L))<5e-9

        tim,tem=switching_counts_mixed(z)
        tin,ten=switching_counts_noshare(z)
        tis,tes=switching_counts_share(z)
        assert tis>tin>tim
        assert tes<ten<tem

        wm=total_welfare(cm,profit_mixed(z),0)
        wn=total_welfare(cn,profit_noshare(z),0)
        ws=total_welfare(cs,profit_share(z),0)
        assert wm>wn>ws

    root_m_ns=brentq(lambda z:f_cs_mixed(z,L)-f_cs_noshare(z,L),ZC+1e-8,1/3-1e-8)
    root_m_s=brentq(lambda z:f_cs_mixed(z,L)-f_cs_share(z,L),ZC+1e-8,1/3-1e-8)
    assert abs(root_m_ns-0.318731295698269)<1e-10
    assert abs(root_m_s-0.320586070246451)<1e-10

    print("primitive_welfare_evaluator=PASS")
    print("cs_mixed_equals_noshare_at",root_m_ns)
    print("cs_mixed_equals_share_at",root_m_s)
    for z in grid:
        print(z,
          "CS",(cs_mixed(z,L),cs_noshare(z,L),cs_share(z,L)),
          "switch",(switching_counts_mixed(z),switching_counts_noshare(z),switching_counts_share(z)),
          "W",(total_welfare(cs_mixed(z,L),profit_mixed(z)),
               total_welfare(cs_noshare(z,L),profit_noshare(z)),
               total_welfare(cs_share(z,L),profit_share(z))))

if __name__=="__main__":
    run()
