from __future__ import annotations
from pathlib import Path
import sympy as sp

OUT = Path("manuscript/generated")
OUT.mkdir(parents=True, exist_ok=True)

z = sp.symbols("z", positive=True)
r = sp.sqrt(3)
zc = sp.simplify((-6 + 4*r) / 3)
KS = ((17 + 9*r)*z**2 - (30 + 18*r)*z + 16) / 9
KNS = ((39 + 18*r)*z**2 - (60 + 36*r)*z + 32) / 18
M = z*((2 + r)*z + 10 + 6*r) / 3
F = 4*(z**2 + 5) / 9
N = (9*z**2 + 40) / 18

L = sp.symbols("L", real=True)
CSM = (24*L + z**2 - 20*z - 8*r*z) / 6
CSNS = (9*z**2 + 72*(2*L + z) - 88) / 36
CSS = (z**2 + 18*(2*L + z) - 22) / 9

def positive_root(expr):
    roots = [x for x in sp.solve(sp.Eq(expr, 0), z)
             if x.is_real and float(sp.N(x)) > 0]
    return min(roots, key=lambda x: float(sp.N(x)))

rows = [
    ("Critical pure-equilibrium threshold", zc),
    ("Sharing investment threshold reaches zero", positive_root(KS)),
    ("No-sharing investment threshold reaches zero", positive_root(KNS)),
    ("Mixed NI profit = sharing-investment profit", positive_root(M-F)),
    ("Mixed NI profit = no-sharing-investment profit", positive_root(M-N)),
    ("Mixed NI CS = no-sharing-investment CS", positive_root(CSM-CSNS)),
    ("Mixed NI CS = sharing-investment CS", positive_root(CSM-CSS)),
]

with (OUT / "key_thresholds.tex").open("w", encoding="utf-8") as f:
    f.write("\\begin{tabular}{p{0.72\\linewidth}r}\\toprule\n")
    f.write("Object & Normalized value \\\\\n")
    f.write("\\midrule\n")
    for label, val in rows:
        f.write(f"{label} & {float(sp.N(val, 16)):.12f} \\\\\n")
    f.write("\\bottomrule\n\\end{tabular}\n")

items = [
    ("1", "Corrected threshold and equality correspondence"),
    ("2", "Corrected threshold and equality correspondence"),
    ("3", "Corrected cost-region classification"),
    ("4", "Survives under certified continuation"),
    ("5", "Corrected profit ranking"),
    ("6", "False globally; corrected CS ranking"),
    ("7", "Survives as outcome-welfare ordering"),
    ("8", "Corrected asymmetric thresholds and boundaries"),
    ("9", "Corrected Stage-I SPE correspondence"),
    ("10", "Welfare logic survives; private threshold corrected"),
]

with (OUT / "results_map.tex").open("w", encoding="utf-8") as f:
    f.write("\\begin{tabular}{cp{0.76\\linewidth}}\\toprule\n")
    f.write("Result & Frozen disposition \\\\\n")
    f.write("\\midrule\n")
    for a, b in items:
        f.write(f"{a} & {b} \\\\\n")
    f.write("\\bottomrule\n\\end{tabular}\n")

print("generated_tables=PASS")
for label, val in rows:
    print(label, float(sp.N(val, 16)))
