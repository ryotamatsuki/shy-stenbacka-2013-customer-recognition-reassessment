from __future__ import annotations
"""
Diagnostic search for alternative high-z mixed equilibria.

This is deliberately NOT a uniqueness proof. It searches the class with at most
two incumbent atoms and at most two poacher atoms, using primitive clipped
payoffs only. A low-regret solution is then checked against continuous
best-response optimization. The intended use is adversarial falsification:
finding a distinct low-regret equilibrium would reopen the downstream
selection analysis; failing to find one does not prove uniqueness.
"""
import math
import numpy as np
from scipy.optimize import differential_evolution

SQ3 = math.sqrt(3.0)
ZC = (-6.0 + 4.0 * SQ3) / 3.0
TYPES = (0.0, 1.0, -1.0, 0.0)

def _clip(x: float) -> float:
    return max(0.0, min(1.0, x))

def incumbent_profit(p: float, q: float, z: float) -> float:
    return sum(p * (1.0 - _clip(p - q - z * sgn)) for sgn in TYPES)

def poacher_profit(q: float, p: float, z: float) -> float:
    return sum(q * _clip(p - q - z * sgn) for sgn in TYPES)

def selected(z: float):
    p = z * (3.0 + 2.0 * SQ3) / 3.0
    qL = p / 2.0
    qH = z * (2.0 + SQ3) / 3.0
    lam = (4.0 - (5.0 + 3.0 * SQ3) * z) / (z * (1.0 + SQ3))
    return p, qL, qH, lam

GRID = np.linspace(0.0, 1.2, 801)

def _inc_grid(q: float, z: float):
    ans = np.zeros_like(GRID)
    for sgn in TYPES:
        ans += GRID * (1.0 - np.clip(GRID - q - z * sgn, 0.0, 1.0))
    return ans

def _poach_grid(p: float, z: float):
    ans = np.zeros_like(GRID)
    for sgn in TYPES:
        ans += GRID * np.clip(p - GRID - z * sgn, 0.0, 1.0)
    return ans

def grid_regret(theta, z: float) -> float:
    p1, p2, a, q1, q2, b = map(float, theta)
    ps, pa = (p1, p2), (a, 1.0-a)
    qs, qb = (q1, q2), (b, 1.0-b)

    eu_i = sum(pa[i] * qb[j] * incumbent_profit(ps[i], qs[j], z)
               for i in range(2) for j in range(2))
    eu_p = sum(pa[i] * qb[j] * poacher_profit(qs[j], ps[i], z)
               for i in range(2) for j in range(2))

    br_i = np.max(qb[0] * _inc_grid(q1, z) + qb[1] * _inc_grid(q2, z))
    br_p = np.max(pa[0] * _poach_grid(p1, z) + pa[1] * _poach_grid(p2, z))
    return max(0.0, float(br_i-eu_i), float(br_p-eu_p))

def continuous_regret(theta, z: float) -> float:
    p1, p2, a, q1, q2, b = map(float, theta)
    ps, pa = (p1, p2), (a, 1.0-a)
    qs, qb = (q1, q2), (b, 1.0-b)

    eu_i = sum(pa[i] * qb[j] * incumbent_profit(ps[i], qs[j], z)
               for i in range(2) for j in range(2))
    eu_p = sum(pa[i] * qb[j] * poacher_profit(qs[j], ps[i], z)
               for i in range(2) for j in range(2))

    ri = differential_evolution(
        lambda X: -(qb[0]*incumbent_profit(float(X[0]), q1, z)
                    + qb[1]*incumbent_profit(float(X[0]), q2, z)),
        [(0.0, 1.2)], seed=991, tol=1e-12, polish=True
    )
    rp = differential_evolution(
        lambda X: -(pa[0]*poacher_profit(float(X[0]), p1, z)
                    + pa[1]*poacher_profit(float(X[0]), p2, z)),
        [(0.0, 1.2)], seed=992, tol=1e-12, polish=True
    )
    return max(0.0, float(-ri.fun-eu_i), float(-rp.fun-eu_p))

def canonicalize(theta):
    p1, p2, a, q1, q2, b = map(float, theta)
    # incumbent atoms ascending, preserving first-atom probability
    if p2 < p1:
        p1, p2, a = p2, p1, 1.0-a
    # poacher atoms ascending, preserving low-atom probability
    if q2 < q1:
        q1, q2, b = q2, q1, 1.0-b
    return p1, p2, a, q1, q2, b

def search(z: float, seed: int):
    bounds = [(0.0,1.1),(0.0,1.1),(0.0,1.0),
              (0.0,1.1),(0.0,1.1),(0.0,1.0)]
    res = differential_evolution(
        lambda th: grid_regret(th, z),
        bounds, seed=seed, popsize=10, maxiter=150, tol=1e-9, polish=True
    )
    th = canonicalize(res.x)
    return {
        "z": z,
        "seed": seed,
        "grid_regret": float(res.fun),
        "continuous_regret": continuous_regret(th, z),
        "theta": th,
        "selected": selected(z),
    }

def run():
    # Interior high-z points where both poaching atoms have economically visible mass.
    rows = [search(z, 20260923) for z in (0.318, 0.325, 0.330)]
    print("stage04a_mixed_alternative_search=DIAGNOSTIC_ONLY")
    print("No uniqueness theorem is inferred from this search.")
    for row in rows:
        print(row)

if __name__ == "__main__":
    run()
