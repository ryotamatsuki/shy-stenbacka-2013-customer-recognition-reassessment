from __future__ import annotations
import sympy as sp

z,k,L=sp.symbols('z k L', positive=True, real=True)
r=sp.sqrt(3)
zc=sp.simplify((-6+4*r)/3)

EI=sp.factor(z*(5+3*r)*(2-z)/3)
EP=sp.factor(z**2*(7+4*r)/3)
M=sp.factor(EI+EP)

I_full=sp.factor((16+2*z**2)/9)
P_full=sp.factor((4+2*z**2)/9)
I_disc=sp.factor(sp.Rational(16,9)+z**2/2)
P_uniform=sp.Rational(4,9)

F=sp.factor(4*(z**2+5)/9)
N=sp.factor((9*z**2+40)/18)
As=sp.factor(I_full+EP)
Bs=sp.factor(P_full+EI)
An=sp.factor(I_disc+EP)
Bn=sp.factor(P_uniform+EI)
CA=sp.factor(I_full+P_uniform)
CB=sp.factor(P_full+I_disc)

KS=sp.factor(As-M)
KNS=sp.factor(An-M)

CS_M=sp.factor((24*L+z**2-20*z-8*r*z)/6)
CS_NS=sp.factor((9*z**2+72*(2*L+z)-88)/36)
CS_S=sp.factor((z**2+18*(2*L+z)-22)/9)

pstar=sp.factor(z*(3+2*r)/3)
qL=sp.factor(pstar/2)
qH=sp.factor(z*(2+r)/3)
lam=sp.factor((4-(5+3*r)*z)/(z*(1+r)))
xL=sp.factor(pstar-qL)
xH=sp.factor(pstar-qH)
TI_M=sp.factor(2*lam*(xL-z))
TE_M=sp.factor(2*(lam*(xL+z)+(1-lam)*(xH+z)))
TI_NS=sp.factor((2-3*z)/3)
TE_NS=sp.factor((2+3*z)/3)
TI_S=sp.factor(2*(1-z)/3)
TE_S=sp.factor(2*(1+z)/3)

W_M=sp.factor(2*CS_M+2*M)
W_NS=sp.factor(2*CS_NS+2*N-2*k)
W_S=sp.factor(2*CS_S+2*F-2*k)

def positive_root(expr):
    roots=[x for x in sp.solve(sp.Eq(expr,0),z) if x.is_real]
    vals=[x for x in roots if sp.N(x)>0]
    return min(vals,key=lambda x:float(sp.N(x)))

zS0=positive_root(KS)
zNS0=positive_root(KNS)
zProfitSF=positive_root(M-F)
zProfitNS=positive_root(M-N)
zCS_NS=positive_root(CS_M-CS_NS)
zCS_S=positive_root(CS_M-CS_S)

def checks():
    assert sp.simplify(KS-(F-Bs))==0
    assert sp.simplify(KNS-(N-Bn))==0
    assert sp.simplify(KNS-KS-5*z**2/18)==0
    assert sp.simplify(CA-Bn-KS)==0
    assert sp.simplify(CB-Bs-KNS)==0
    assert sp.simplify(TI_S-TI_NS-z/3)==0
    assert sp.simplify(TE_NS-TE_S-z/3)==0
    assert float(sp.N(zS0)) > float(sp.N(zc))
    assert float(sp.N(zNS0)) > float(sp.N(zS0))
    assert float(sp.N(zNS0)) < 1/3
    assert sp.simplify(W_NS-W_S-7*z**2/18)==0
    return {
      'zc':zc,
      'KS':KS,'KNS':KNS,
      'zS0':zS0,'zNS0':zNS0,
      'zProfit_M_equals_S':zProfitSF,
      'zProfit_M_equals_NS':zProfitNS,
      'zCS_M_equals_NS':zCS_NS,
      'zCS_M_equals_S':zCS_S,
      'TI_M':TI_M,'TE_M':TE_M,
      'CS_M_minus_NS':sp.factor(CS_M-CS_NS),
      'W_M_minus_NS':sp.factor(W_M-W_NS),
    }

if __name__=='__main__':
    out=checks()
    print('backward_induction_symbolics=PASS')
    for key,val in out.items():
        print(key,'=',val,'~',sp.N(val) if not hasattr(val,'free_symbols') or not val.free_symbols else '')
