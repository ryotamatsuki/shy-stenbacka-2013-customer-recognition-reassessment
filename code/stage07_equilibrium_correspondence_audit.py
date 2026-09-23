from __future__ import annotations
import sympy as sp

z,k=sp.symbols("z k", nonnegative=True, real=True)
r=sp.sqrt(3)
zc=sp.simplify(-2+4*r/3)

# Safe continuation components.
I_full=(16+2*z**2)/9
P_full=(4+2*z**2)/9
I_disc=sp.Rational(16,9)+z**2/2
P_uniform=sp.Rational(4,9)

F=sp.factor(4*(z**2+5)/9)
N=sp.factor((9*z**2+40)/18)

# High-z selected mixed UU continuation.
EI=sp.factor(z*(5+3*r)*(2-z)/3)
EP=sp.factor(z**2*(7+4*r)/3)
M=sp.factor(EI+EP)

As=sp.factor(I_full+EP)
Bs=sp.factor(P_full+EI)
An=sp.factor(I_disc+EP)
Bn=sp.factor(P_uniform+EI)
CA=sp.factor(I_full+P_uniform)
CB=sp.factor(P_full+I_disc)

KS=sp.factor(As-M)
KNS=sp.factor(An-M)

# Stage-II dominance thresholds from both columns of each 2x2 investment game.
assert sp.simplify(F-Bs-KS)==0
assert sp.simplify(As-M-KS)==0
assert sp.simplify(N-Bn-KNS)==0
assert sp.simplify(An-M-KNS)==0

# Asymmetric (S,NS): sharer threshold KS, non-sharer threshold KNS.
assert sp.simplify(CA-Bn-KS)==0
assert sp.simplify(CB-Bs-KNS)==0

# Threshold ordering and continuity.
assert sp.simplify(KNS-KS-5*z**2/18)==0
KS_low=2*z**2/9
KNS_low=z**2/2
assert sp.simplify(KS.subs(z,zc)-KS_low.subs(z,zc))==0
assert sp.simplify(KNS.subs(z,zc)-KNS_low.subs(z,zc))==0

# Stage-I strict no-sharing incentives.
# Region k<KS: both histories induce investment.
assert sp.simplify(CB-F-5*z**2/18)==0
assert sp.simplify(N-CA-5*z**2/18)==0
# Region KS<k<KNS: deviating to NS makes the non-sharer invest.
assert sp.simplify((An-k)-M-(KNS-k))==0
assert sp.simplify((N-k)-Bn-(KNS-k))==0

# At k=KS, even the least favorable equilibrium continuation after a deviation
# to NS beats the most favorable SS payoff on the high-z positive-KS wedge.
boundary_gain_hi=sp.factor(An-F)
# Positive on z in [zc, root(KS)] because its unique positive root is below zc.
boundary_gain_hi_root=sp.simplify(2*sp.sqrt(2)/sp.sqrt(24*r+43))
assert float(sp.N(boundary_gain_hi_root)) < float(sp.N(zc))

# Low-z counterpart at k=KS: source pure UU continuation M0=20/9.
M0=sp.Rational(20,9)
KS0=2*z**2/9
KNS0=z**2/2
Bs0=M0+KS0
An0=M0+KNS0
# minimum deviation payoff minus maximum SS payoff = KNS0-KS0-KS0? 
# At asymmetric history, choose sharer NI, so deviating non-sharer gets An0-KS0.
# At SS, the maximum own payoff is Bs0.
assert sp.simplify((An0-KS0)-Bs0-z**2/18)==0

# Profit crossings.
profit_M_minus_F=sp.factor(M-F)
profit_M_minus_N=sp.factor(M-N)

# Consumer surplus and total welfare identities.
L=sp.symbols("L", real=True)
CS_M=sp.factor((24*L+z**2-20*z-8*r*z)/6)
CS_NS=sp.factor((9*z**2+72*(2*L+z)-88)/36)
CS_S=sp.factor((z**2+18*(2*L+z)-22)/9)
assert sp.simplify(CS_NS-CS_S-5*z**2/36)==0

W_M=sp.factor(2*CS_M+2*M)
W_NS=sp.factor(2*CS_NS+2*N-2*k)
W_S=sp.factor(2*CS_S+2*F-2*k)
assert sp.simplify(W_NS-W_S-7*z**2/18)==0
Wgap=sp.factor(W_M-W_NS)

# Switching-order identities under selected continuation.
pstar=sp.factor(z*(3+2*r)/3)
qL=sp.factor(pstar/2)
qH=sp.factor(z*(2+r)/3)
lam=sp.factor((4-(5+3*r)*z)/(z*(1+r)))
xL=sp.factor(pstar-qL)
xH=sp.factor(pstar-qH)
TI_M=sp.factor(2*lam*(xL-z))
TE_M=sp.factor(2*(lam*(xL+z)+(1-lam)*(xH+z)))
TI_NS=(2-3*z)/3
TE_NS=(2+3*z)/3
TI_S=2*(1-z)/3
TE_S=2*(1+z)/3
assert sp.simplify(TI_S-TI_NS-z/3)==0
assert sp.simplify(TE_NS-TE_S-z/3)==0

def positive_root(expr):
    roots=[x for x in sp.solve(sp.Eq(expr,0),z) if x.is_real and sp.N(x)>0]
    return min(roots,key=lambda x:float(sp.N(x)))

if __name__=="__main__":
    zS0=positive_root(KS)
    zNS0=positive_root(KNS)
    zPF=positive_root(profit_M_minus_F)
    zPN=positive_root(profit_M_minus_N)
    zCNS=positive_root(CS_M-CS_NS)
    zCS=positive_root(CS_M-CS_S)

    assert float(sp.N(zc)) < float(sp.N(zS0)) < float(sp.N(zNS0)) < 1/3
    assert float(sp.N(zc)) < float(sp.N(zPF)) < float(sp.N(zPN)) < 1/3
    assert float(sp.N(zc)) < float(sp.N(zCNS)) < float(sp.N(zCS)) < 1/3

    # W_M-W_NS is minimized at the upper boundary over the maintained high-z wedge:
    # its z-derivative is negative throughout z<1/3, and k enters positively.
    dWdz=sp.factor(sp.diff(Wgap,z))
    assert float(sp.N(dWdz.subs({z:zc,k:0}))) < 0
    assert float(sp.N(dWdz.subs({z:sp.Rational(1,3),k:0}))) < 0
    assert float(sp.N(Wgap.subs({z:sp.Rational(1,3),k:0}))) > 0

    # Switching rankings at both high-z endpoints; analytic differences are affine.
    for zz in (zc,sp.Rational(1,3)):
        assert float(sp.N((TI_NS-TI_M).subs(z,zz))) > 0
        assert float(sp.N((TE_M-TE_NS).subs(z,zz))) > 0

    print("stage07_equilibrium_correspondence_audit=PASS")
    print("zc",sp.N(zc,18))
    print("KS_zero",sp.N(zS0,18))
    print("KNS_zero",sp.N(zNS0,18))
    print("profit_M_eq_F",sp.N(zPF,18))
    print("profit_M_eq_N",sp.N(zPN,18))
    print("CS_M_eq_NS",sp.N(zCNS,18))
    print("CS_M_eq_S",sp.N(zCS,18))
    print("boundary_gain_hi_root",sp.N(boundary_gain_hi_root,18))
    print("Wgap_at_upper_k0",sp.N(Wgap.subs({z:sp.Rational(1,3),k:0}),18))
