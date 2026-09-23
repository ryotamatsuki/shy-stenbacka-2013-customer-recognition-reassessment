"""Independent Stage-1 reproduction for Shy & Stenbacka (2013) reassessment.

Does not import the historical ozshypapers audit. Starts from valuation
differences, the no-information candidate, and clipped switching shares.
"""
from fractions import Fraction
import sympy as sp

Delta, sigma, q = sp.symbols("Delta sigma q", positive=True)
dvals = (sp.Integer(0), Delta, -Delta, sp.Integer(0))

p0 = 2*sigma/3
q0 = sigma/3
D0 = sp.simplify(sum((p0-q0+d)/sigma for d in dvals))
R0 = sp.simplify(q0*D0)
assert sp.simplify(D0-sp.Rational(4,3)) == 0
assert sp.simplify(R0-4*sigma/9) == 0

# In the branch reached after the d=-Delta group is clipped at zero.
R3 = sp.expand(q*((p0-q)/sigma + (p0-q+Delta)/sigma + (p0-q)/sigma))
qstar = sp.solve(sp.diff(R3,q),q)[0]
Rstar = sp.factor(R3.subs(q,qstar))
gain = sp.factor(Rstar-R0)
zc = sp.simplify((-6+4*sp.sqrt(3))/3)

assert sp.simplify(qstar-(2*sigma+Delta)/6) == 0
assert sp.simplify(Rstar-(2*sigma+Delta)**2/(12*sigma)) == 0
assert sp.simplify(gain-(3*Delta**2+12*Delta*sigma-4*sigma**2)/(36*sigma)) == 0

subs={sigma:sp.Integer(25),Delta:sp.Integer(8)}
assert q0.subs(subs)==sp.Rational(25,3)
assert qstar.subs(subs)==sp.Rational(29,3)
assert gain.subs(subs)==sp.Rational(23,225)

# Independent exact direct-payoff calculation using rational clipping.
p=Fraction(50,3); D=Fraction(8); sig=Fraction(25)
def clip(x): return max(Fraction(0),min(Fraction(1),x))
def rev(qv):
    return qv*sum(clip((p-qv+d)/sig) for d in
                   (Fraction(0),D,-D,Fraction(0)))
assert rev(Fraction(29,3))-rev(Fraction(25,3))==Fraction(23,225)

print("STAGE01_EXACT_COUNTEREXAMPLE=PASS")
print("gain=",gain)
print("zc=",zc)
print("sigma25_Delta8_gain=",gain.subs(subs))
