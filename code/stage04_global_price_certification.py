from __future__ import annotations
import sympy as sp

z = sp.symbols("z", positive=True, real=True)
r = sp.sqrt(3)
zc = sp.simplify((-6 + 4*r)/3)

# UU smooth-branch candidates for F_z(x)=a*x+b.
def smooth_candidate(a, b):
    p = sp.simplify((8-b)/(3*a))
    q = sp.simplify((4+b)/(3*a))
    x = sp.simplify(p-q)
    return p, q, x

# Interior branches, ordered from low to high x.
branches = {
    "[-z,0]": (1, z),
    "[0,z]": (3, z),
    "[z,1-z]": (4, 0),
    "[1-z,1]": (3, 1-z),
    "[1,1+z]": (1, 3-z),
}

cand = {name: smooth_candidate(a,b) for name,(a,b) in branches.items()}

# Source candidate is the only smooth feasible mutual candidate under 0<z<1/3.
assert sp.simplify(cand["[z,1-z]"][0] - sp.Rational(2,3)) == 0
assert sp.simplify(cand["[z,1-z]"][1] - sp.Rational(1,3)) == 0
assert sp.simplify(cand["[z,1-z]"][2] - sp.Rational(1,3)) == 0

# Other smooth branches violate their own x intervals throughout 0<z<1/3.
# [-z,0] candidate has x>0.
assert sp.factor(cand["[-z,0]"][2]) == sp.factor(2*(2-z)/3)
# [0,z] candidate exceeds z because x-z=(4-11z)/9>0 for z<1/3.
assert sp.factor(cand["[0,z]"][2]-z) == sp.factor((4-11*z)/9)
# [1-z,1] candidate lies below 1-z because (1-z)-x=(7-11z)/9>0.
assert sp.factor((1-z)-cand["[1-z,1]"][2]) == sp.factor((7-11*z)/9)
# [1,1+z] candidate has x<0.
assert sp.factor(cand["[1,1+z]"][2]) == sp.factor(2*(z-1)/3)

# Exact global poaching comparison at the source incumbent p=2/3.
q0 = sp.Rational(1,3)
qH = sp.simplify((2+z)/6)
pi0 = sp.Rational(4,9)
piH = sp.simplify((2+z)**2/12)
gain = sp.factor(piH-pi0)
assert gain == sp.factor((3*z**2+12*z-4)/36)
assert sp.simplify((3*zc**2+12*zc-4)) == 0
assert sp.simplify(gain.subs(z,sp.Rational(8,25))*25 - sp.Rational(23,225)) == 0

# TT component: one type-specific incumbent price p and poaching price q.
d = sp.symbols("d", real=True)
pTT = sp.simplify((2+d)/3)
qTT = sp.simplify((1-d)/3)
sTT = sp.simplify(pTT-qTT-d)
assert sp.simplify(sTT-(1-d)/3) == 0
# Against qTT, incumbent's interior quadratic vertex is exactly pTT.
assert sp.simplify((1+qTT+d)/2-pTT) == 0
# Against pTT, poacher's interior quadratic vertex is exactly qTT.
assert sp.simplify((pTT-d)/2-qTT) == 0

# TU component: type-specific incumbents p_t against a common poaching q.
qTU = sp.Rational(1,3)
pTU = sp.simplify(sp.Rational(2,3)+d/2)
sTU = sp.simplify(pTU-qTU-d)
assert sp.simplify(sTU-(sp.Rational(1,3)-d/2)) == 0
assert sp.simplify((1+qTU+d)/2-pTU) == 0

# Once the d=+z group drops, the 3-active poaching branch has its vertex
# strictly to the left of the branch boundary for every z<1/3.
tu_drop_boundary = sp.simplify(sp.Rational(2,3)-z/2)
tu_three_vertex = sp.simplify(sp.Rational(1,3)+z/12)
assert sp.factor(tu_drop_boundary-tu_three_vertex) == sp.factor(sp.Rational(1,3)-7*z/12)
# After d=0 groups also drop, the final one-active vertex is also left of its region.
tu_one_vertex = sp.simplify(sp.Rational(1,3)+z/4)
assert sp.factor(sp.Rational(2,3)-tu_one_vertex) == sp.factor(sp.Rational(1,3)-z/4)

# High-z selected symmetric semi-mixed UU continuation.
pstar = sp.simplify(z*(3+2*r)/3)
qL = sp.simplify(pstar/2)
qHi = sp.simplify(z*(2+r)/3)
lam = sp.simplify((4-(5+3*r)*z)/(z*(1+r)))
xL = sp.simplify(pstar-qL)
xH = sp.simplify(pstar-qHi)

piL = sp.simplify(qL*(4*xL))
piHi = sp.simplify(qHi*(3*xH+z))
assert sp.simplify(piL-piHi) == 0
assert sp.simplify(pstar.subs(z,zc)-sp.Rational(2,3)) == 0
assert sp.simplify(qL.subs(z,zc)-sp.Rational(1,3)) == 0
assert sp.simplify(lam.subs(z,zc)-1) == 0
assert sp.simplify(sp.diff(lam,z) + 4/(z**2*(1+r))) == 0

EI = sp.factor(z*(5+3*r)*(2-z)/3)
EP = sp.factor(z**2*(7+4*r)/3)
M = sp.factor(EI+EP)

if __name__ == "__main__":
    print("stage04_symbolic_globality_certificate=PASS")
    print("zc =", zc)
    print("UU source =", (sp.Rational(2,3),sp.Rational(1,3)))
    print("gain =", gain)
    print("mixed =", (pstar,qL,qHi,lam))
    print("mixed_component_payoffs =", (EI,EP))
    print("mixed_firm_payoff =", M)
