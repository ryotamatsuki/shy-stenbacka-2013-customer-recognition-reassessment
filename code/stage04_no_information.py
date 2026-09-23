from __future__ import annotations
import math
from dataclasses import dataclass
from fractions import Fraction
import sympy as sp

sqrt3 = sp.sqrt(3)
z = sp.symbols('z', positive=True, real=True)

ZC = sp.simplify((-6 + 4*sqrt3)/3)


def clip_sym(x):
    return sp.Min(1, sp.Max(0, x))


def F_piecewise(x, z_):
    """Aggregate switching mass for four valuation differences 0,0,+z,-z, sigma=1."""
    return 2*sp.Min(1, sp.Max(0, x)) + sp.Min(1, sp.Max(0, x+z_)) + sp.Min(1, sp.Max(0, x-z_))


def gain_source_to_three_active(z_):
    return sp.factor((3*z_**2 + 12*z_ - 4)/36)


def mixed_prices(z_):
    p = sp.simplify(z_*(3+2*sqrt3)/3)
    qL = sp.simplify(p/2)
    qH = sp.simplify(z_*(2+sqrt3)/3)
    lam = sp.simplify((4-(5+3*sqrt3)*z_)/(z_*(1+sqrt3)))
    return p,qL,qH,lam


def mixed_pair_payoffs(z_):
    p,qL,qH,lam = mixed_prices(z_)
    xL = sp.simplify(p-qL)
    xH = sp.simplify(p-qH)
    FL = sp.simplify(4*xL)
    FH = sp.simplify(3*xH+z_)
    incumbent = sp.factor(lam*p*(4-FL) + (1-lam)*p*(4-FH))
    poacher = sp.factor(qL*FL)
    total = sp.factor(incumbent+poacher)
    return incumbent,poacher,total


def continuation_payoffs(z_):
    EI,EP,M = mixed_pair_payoffs(z_)
    I_full = sp.factor((16+2*z_**2)/9)
    P_full = sp.factor((4+2*z_**2)/9)
    I_disc = sp.factor(sp.Rational(16,9)+z_**2/2)
    P_uniform = sp.Rational(4,9)
    full_both = sp.factor(4*(z_**2+5)/9)
    no_share_both = sp.factor((9*z_**2+40)/18)
    one_shared_investor = sp.factor(I_full+EP)
    one_shared_noninvestor = sp.factor(P_full+EI)
    one_private_investor = sp.factor(I_disc+EP)
    one_private_noninvestor = sp.factor(P_uniform+EI)
    asym_sharer_both = sp.factor(I_full+P_uniform)
    asym_nonsharer_both = sp.factor(P_full+I_disc)
    return {
        'NI': M,
        'S_both_I': full_both,
        'NS_both_I': no_share_both,
        'one_shared_investor': one_shared_investor,
        'one_shared_noninvestor': one_shared_noninvestor,
        'one_private_investor': one_private_investor,
        'one_private_noninvestor': one_private_noninvestor,
        'asym_both_sharer': asym_sharer_both,
        'asym_both_nonsharer': asym_nonsharer_both,
    }


def corrected_thresholds(z_):
    P=continuation_payoffs(z_)
    KS = sp.factor(P['one_shared_investor']-P['NI'])
    KNS = sp.factor(P['one_private_investor']-P['NI'])
    assert sp.simplify(KS-(P['S_both_I']-P['one_shared_noninvestor'])) == 0
    assert sp.simplify(KNS-(P['NS_both_I']-P['one_private_noninvestor'])) == 0
    return KS,KNS


def symbolic_checks():
    zz=sp.Rational(8,25)
    g=sp.factor(gain_source_to_three_active(zz))
    assert g == sp.Rational(23,5625)
    assert sp.simplify(25*g-sp.Rational(23,225)) == 0

    p,qL,qH,lam=mixed_prices(z)
    xL=sp.simplify(p-qL); xH=sp.simplify(p-qH)
    assert sp.simplify(qL*(4*xL)-qH*(3*xH+z)) == 0
    assert sp.simplify(xL/z - (sp.Rational(1,2)+sqrt3/3)) == 0
    assert sp.simplify(xH/z - (sp.Rational(1,3)+sqrt3/3)) == 0
    assert sp.simplify(p.subs(z,ZC)-sp.Rational(2,3)) == 0
    assert sp.simplify(qL.subs(z,ZC)-sp.Rational(1,3)) == 0
    assert sp.simplify(lam.subs(z,ZC)-1) == 0

    KS,KNS=corrected_thresholds(z)
    assert sp.simplify((KNS-KS)-5*z**2/18) == 0
    assert sp.simplify(KS.subs(z,ZC)-2*ZC**2/9) == 0
    assert sp.simplify(KNS.subs(z,ZC)-ZC**2/2) == 0
    return {
        'zc': sp.simplify(ZC),
        'mixed_prices': tuple(sp.factor(x) for x in mixed_prices(z)),
        'pair_payoffs': tuple(sp.factor(x) for x in mixed_pair_payoffs(z)),
        'thresholds': tuple(sp.factor(x) for x in corrected_thresholds(z)),
        'continuation_payoffs': continuation_payoffs(z),
    }


if __name__ == '__main__':
    out=symbolic_checks()
    print('symbolic_checks=PASS')
    for k,v in out.items():
        print(k,'=',v)
