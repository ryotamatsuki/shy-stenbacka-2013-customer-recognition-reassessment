from __future__ import annotations
"""
Stage 7.5A diagnostic portability attacks.

These tests do NOT alter the canonical Shy–Stenbacka baseline model.
They ask whether the headline pure-nonexistence mechanism survives two
pre-specified economically meaningful perturbations.

Attack A: replace uniform switching costs by Beta(2,2) on [0,1].
Attack B: retain uniform switching costs but perturb type masses from
          (1,1,1,1) to (1,1.25,0.75,1).

For each alternative, re-solve the one-base UU price game on a dense price
grid and compute maximum unilateral grid regret. Finding low-regret pure
profiles throughout the upper-z region falsifies any claim that baseline
pure nonexistence is portable to these alternatives.

This is diagnostic numerical evidence, not a proof of existence/uniqueness
in the alternative games.
"""
import numpy as np

TYPES=np.array([0.0,1.0,-1.0,0.0])

def H_uniform(x):
    return np.clip(x,0.0,1.0)

def H_beta22(x):
    y=np.clip(x,0.0,1.0)
    return np.where(x<=0.0,0.0,np.where(x>=1.0,1.0,3*y*y-2*y*y*y))

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
    return {
      "z":float(z),
      "p":float(P[idx[0]]),
      "q":float(Q[idx[1]]),
      "grid_regret":float(regret[idx]),
    }

def run():
    zgrid=(0.31,0.32,0.33)

    beta=[]
    for z in zgrid:
        beta.append(solve_grid(z,H_beta22,np.ones(4)))
    unequal=[]
    masses=np.array([1.0,1.25,0.75,1.0])
    for z in zgrid:
        unequal.append(solve_grid(z,H_uniform,masses))

    # Both pre-specified alternatives retain near-zero-regret pure profiles
    # in the region where the baseline uniform/equal-mass game has no pure NE.
    assert max(r["grid_regret"] for r in beta) < 1e-8
    assert max(r["grid_regret"] for r in unequal) < 1e-8

    print("stage075a_portability_attacks=PASS")
    print("classification=baseline_pure_nonexistence_MODEL_SPECIFIC")
    print("beta22_rows")
    for r in beta: print(r)
    print("unequal_mass_rows")
    for r in unequal: print(r)

if __name__=="__main__":
    run()
