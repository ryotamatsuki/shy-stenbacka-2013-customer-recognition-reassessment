from __future__ import annotations
"""
Stage 7.5A diagnostic portability attacks — continuous-best-response version.

These tests do NOT alter the canonical Shy–Stenbacka baseline model.
They test whether the baseline high-z pure-nonexistence conclusion survives two
pre-specified, economically meaningful perturbations.

Attack A: replace uniform switching costs by Beta(2,2) on [0,1].
Attack B: retain uniform switching costs but perturb type masses from
          (1,1,1,1) to (1,1.25,0.75,1).

A Stage-11 certification regression found that the original implementation
reported only grid regret. This version uses the grid only to initialize the
search, then alternates continuous best responses computed by deterministic
differential evolution and finally measures continuous unilateral regret.
"""
import numpy as np
from scipy.optimize import differential_evolution

TYPES=np.array([0.0,1.0,-1.0,0.0])
PRICE_HI=2.0

def H_uniform(x):
    return np.clip(x,0.0,1.0)

def H_beta22(x):
    y=np.clip(x,0.0,1.0)
    return np.where(x<=0.0,0.0,np.where(x>=1.0,1.0,3*y*y-2*y*y*y))

def payoffs(p,q,z,H,masses):
    x=p-q-z*TYPES
    sw=H(x)
    ui=p*np.sum(masses*(1.0-sw))
    up=q*np.sum(masses*sw)
    return float(ui),float(up)

def solve_grid(z,H,masses,n=801,hi=1.2):
    P=np.linspace(0.0,hi,n)
    Q=np.linspace(0.0,hi,n)
    p=P[:,None,None]
    q=Q[None,:,None]
    x=p-q-z*TYPES[None,None,:]
    sw=H(x)
    ui=p[:,:,0]*np.sum(masses[None,None,:]*(1.0-sw),axis=2)
    up=q[:,:,0]*np.sum(masses[None,None,:]*sw,axis=2)
    inc_regret=np.max(ui,axis=0)[None,:]-ui
    poach_regret=np.max(up,axis=1)[:,None]-up
    regret=np.maximum(inc_regret,poach_regret)
    idx=np.unravel_index(np.argmin(regret),regret.shape)
    return float(P[idx[0]]),float(Q[idx[1]]),float(regret[idx])

def best_incumbent(q,z,H,masses):
    r=differential_evolution(
        lambda X:-payoffs(float(X[0]),q,z,H,masses)[0],
        [(0.0,PRICE_HI)],seed=20260931,tol=1e-12,polish=True
    )
    if not r.success or not np.isfinite(r.fun) or not np.isfinite(r.x[0]):
        raise RuntimeError(f'incumbent best-response optimizer failed: {r.message}')
    return float(r.x[0]),float(-r.fun)

def best_poacher(p,z,H,masses):
    r=differential_evolution(
        lambda X:-payoffs(p,float(X[0]),z,H,masses)[1],
        [(0.0,PRICE_HI)],seed=20260932,tol=1e-12,polish=True
    )
    if not r.success or not np.isfinite(r.fun) or not np.isfinite(r.x[0]):
        raise RuntimeError(f'poacher best-response optimizer failed: {r.message}')
    return float(r.x[0]),float(-r.fun)

def continuous_refine(z,H,masses):
    p,q,grid_regret=solve_grid(z,H,masses)
    for _ in range(60):
        p_new,_=best_incumbent(q,z,H,masses)
        q_new,_=best_poacher(p_new,z,H,masses)
        if abs(p_new-p)+abs(q_new-q)<1e-11:
            p,q=p_new,q_new
            break
        p,q=p_new,q_new

    ui,up=payoffs(p,q,z,H,masses)
    pbr,ui_br=best_incumbent(q,z,H,masses)
    qbr,up_br=best_poacher(p,z,H,masses)
    continuous_regret=max(0.0,ui_br-ui,up_br-up)
    return {
      "z":float(z),
      "p":p,
      "q":q,
      "grid_regret":grid_regret,
      "p_br":pbr,
      "q_br":qbr,
      "continuous_regret":continuous_regret,
    }

def run():
    zgrid=(0.31,0.32,0.33)

    beta=[continuous_refine(z,H_beta22,np.ones(4)) for z in zgrid]
    unequal_masses=np.array([1.0,1.25,0.75,1.0])
    unequal=[continuous_refine(z,H_uniform,unequal_masses) for z in zgrid]

    # Continuous, not merely grid, unilateral deviations are now attacked.
    assert max(r["continuous_regret"] for r in beta) < 1e-8
    assert max(r["continuous_regret"] for r in unequal) < 1e-8

    print("stage075a_portability_attacks=PASS_CONTINUOUS_BR")
    print("classification=baseline_pure_nonexistence_MODEL_SPECIFIC")
    print("beta22_rows")
    for r in beta: print(r)
    print("unequal_mass_rows")
    for r in unequal: print(r)

if __name__=="__main__":
    run()
