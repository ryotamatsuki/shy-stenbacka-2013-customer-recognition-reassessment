import Mathlib

namespace SS2013Reassessment

/-!
Targeted formal verification for the Shy–Stenbacka (2013) reassessment.

Model boundary:
* The Stage-4/4A economic audit constructs and independently attacks the clipped
  demand correspondence and the global best-response partition.
* This file kernel-checks proof-critical algebra: the kink gain, critical root,
  exact rational counterexample, mixed-support indifference, corrected
  investment-threshold identities, and selected welfare accounting.
* It does not claim a formalization of the full continuum consumer model,
  branch exhaustiveness, or uniqueness of the mixed equilibrium.
-/

noncomputable section

open Real

def zCritical : ℝ := (-6 + 4 * Real.sqrt 3) / 3

def zNegative : ℝ := (-6 - 4 * Real.sqrt 3) / 3

def gainNorm (z : ℝ) : ℝ :=
  (3*z^2 + 12*z - 4) / 36

def gainDim (Delta sigma : ℝ) : ℝ :=
  (3*Delta^2 + 12*Delta*sigma - 4*sigma^2) / (36*sigma)

theorem sqrt_three_sq : (Real.sqrt 3)^2 = (3 : ℝ) := by
  have h : (0 : ℝ) ≤ 3 := by norm_num
  simpa using Real.sq_sqrt h

theorem sqrt_three_pos : (0 : ℝ) < Real.sqrt 3 := by
  exact Real.sqrt_pos.2 (by norm_num)

theorem critical_is_root :
    3*zCritical^2 + 12*zCritical - 4 = 0 := by
  unfold zCritical
  nlinarith [sqrt_three_sq]

theorem negative_is_root :
    3*zNegative^2 + 12*zNegative - 4 = 0 := by
  unfold zNegative
  nlinarith [sqrt_three_sq]

theorem negative_root_is_negative : zNegative < 0 := by
  unfold zNegative
  nlinarith [sqrt_three_pos]

theorem gain_numerator_factor (z : ℝ) :
    3*z^2 + 12*z - 4 = 3 * (z-zCritical) * (z-zNegative) := by
  unfold zCritical zNegative
  nlinarith [sqrt_three_sq]

theorem gain_positive_above_critical
    (z : ℝ) (hz : 0 < z) (hc : zCritical < z) :
    0 < gainNorm z := by
  have hn : zNegative < z := lt_trans negative_root_is_negative hz
  have h1 : 0 < z - zCritical := sub_pos.mpr hc
  have h2 : 0 < z - zNegative := sub_pos.mpr hn
  have hprod : 0 < 3 * (z-zCritical) * (z-zNegative) := by positivity
  have hnum : 0 < 3*z^2 + 12*z - 4 := by
    rw [gain_numerator_factor]
    exact hprod
  unfold gainNorm
  positivity

theorem exact_counterexample_gain :
    gainDim 8 25 = (23 : ℝ) / 225 := by
  norm_num [gainDim]

theorem exact_counterexample_positive :
    (0 : ℝ) < gainDim 8 25 := by
  rw [exact_counterexample_gain]
  norm_num

def pStar (z : ℝ) : ℝ :=
  z * (3 + 2*Real.sqrt 3) / 3

def qLow (z : ℝ) : ℝ :=
  pStar z / 2

def qHigh (z : ℝ) : ℝ :=
  z * (2 + Real.sqrt 3) / 3

def poachLowProfit (z : ℝ) : ℝ :=
  qLow z * (4 * (pStar z - qLow z))

def poachHighProfit (z : ℝ) : ℝ :=
  qHigh z * (3 * (pStar z - qHigh z) + z)

theorem mixed_support_indifference (z : ℝ) :
    poachLowProfit z = poachHighProfit z := by
  unfold poachLowProfit poachHighProfit qLow qHigh pStar
  ring_nf
  nlinarith [sqrt_three_sq]

def kShare (z : ℝ) : ℝ :=
  ((17 + 9*Real.sqrt 3)*z^2
    - (30 + 18*Real.sqrt 3)*z + 16) / 9

def kNoShare (z : ℝ) : ℝ :=
  ((39 + 18*Real.sqrt 3)*z^2
    - (60 + 36*Real.sqrt 3)*z + 32) / 18

theorem corrected_threshold_gap (z : ℝ) :
    kNoShare z - kShare z = 5*z^2/18 := by
  unfold kNoShare kShare
  ring

def profitMix (z : ℝ) : ℝ :=
  z * ((2 + Real.sqrt 3)*z + 10 + 6*Real.sqrt 3) / 3

def profitShare (z : ℝ) : ℝ :=
  4*(z^2+5)/9

def profitNoShare (z : ℝ) : ℝ :=
  (9*z^2+40)/18

theorem noShare_minus_share_profit (z : ℝ) :
    profitNoShare z - profitShare z = z^2/18 := by
  unfold profitNoShare profitShare
  ring

def csMix (L z : ℝ) : ℝ :=
  (24*L + z^2 - 20*z - 8*Real.sqrt 3*z) / 6

def csNoShare (L z : ℝ) : ℝ :=
  (9*z^2 + 72*(2*L+z) - 88) / 36

def csShare (L z : ℝ) : ℝ :=
  (z^2 + 18*(2*L+z) - 22) / 9

theorem cs_noShare_minus_share (L z : ℝ) :
    csNoShare L z - csShare L z = 5*z^2/36 := by
  unfold csNoShare csShare
  ring

def totalMix (L z : ℝ) : ℝ :=
  2*csMix L z + 2*profitMix z

def totalNoShare (L z k : ℝ) : ℝ :=
  2*csNoShare L z + 2*profitNoShare z - 2*k

def totalShare (L z k : ℝ) : ℝ :=
  2*csShare L z + 2*profitShare z - 2*k

theorem total_noShare_minus_share (L z k : ℝ) :
    totalNoShare L z k - totalShare L z k = 7*z^2/18 := by
  unfold totalNoShare totalShare csNoShare csShare profitNoShare profitShare
  ring

#print axioms critical_is_root
#print axioms gain_numerator_factor
#print axioms gain_positive_above_critical
#print axioms exact_counterexample_gain
#print axioms mixed_support_indifference
#print axioms corrected_threshold_gap
#print axioms noShare_minus_share_profit
#print axioms cs_noShare_minus_share
#print axioms total_noShare_minus_share

end
end SS2013Reassessment
