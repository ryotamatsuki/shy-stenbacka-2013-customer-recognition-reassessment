from __future__ import annotations
from pathlib import Path
import re

ROOT=Path(".")
MAN=ROOT/"manuscript"
SUB=ROOT/"submission"

required=[
    MAN/"main.tex",
    MAN/"references.bib",
    MAN/"sections/00_abstract.tex",
    MAN/"sections/11_declarations.tex",
    MAN/"sections/11_ai_declaration.tex",
    SUB/"title_page.md",
    SUB/"cover_letter.md",
    SUB/"highlights.txt",
    SUB/"declarations.md",
    SUB/"JOURNAL_REQUIREMENTS_IEP.md",
]
for p in required:
    assert p.exists(), f"missing required submission file: {p}"

main=(MAN/"main.tex").read_text(encoding="utf-8")
abstract=(MAN/"sections/00_abstract.tex").read_text(encoding="utf-8")
high=(SUB/"highlights.txt").read_text(encoding="utf-8").splitlines()
cover=(SUB/"cover_letter.md").read_text(encoding="utf-8")
all_tex="\n".join(p.read_text(encoding="utf-8") for p in sorted((MAN/"sections").glob("*.tex")))

# Keywords: max 6.
m=re.search(r"\\textbf\{Keywords:\}\s*(.+)",abstract)
assert m, "keywords line missing"
keywords=[x.strip() for x in m.group(1).split(";") if x.strip()]
assert 1 <= len(keywords) <= 6, f"keyword count {len(keywords)}"

# Abstract: conservative 250-word check after removing simple TeX/math markup.
a=re.sub(r"\\begin\{abstract\}|\\end\{abstract\}", " ", abstract)
a=a.split("\\noindent\\textbf{Keywords:}")[0]
a=re.sub(r"\\[A-Za-z]+(?:\{[^}]*\})?", " ", a)
a=re.sub(r"[^A-Za-z0-9'-]+", " ", a)
abstract_words=[x for x in a.split() if x]
assert len(abstract_words) <= 250, f"abstract too long: {len(abstract_words)} words"

# Highlights: 3-5, <=85 chars excluding bullet marker/leading spaces.
hl=[]
for line in high:
    line=line.strip()
    if not line or line.lower()=="highlights":
        continue
    line=re.sub(r"^[•*-]\s*", "", line)
    hl.append(line)
assert 3 <= len(hl) <= 5, f"highlight count {len(hl)}"
for line in hl:
    assert len(line) <= 85, f"highlight too long ({len(line)}): {line}"

# AI declaration ordering: included after declarations and immediately before references.
idx_decl=main.index("\\input{sections/11_declarations}")
idx_ai=main.index("\\input{sections/11_ai_declaration}")
idx_bib=main.index("\\bibliographystyle")
assert idx_decl < idx_ai < idx_bib, "declaration/AI/reference ordering incorrect"

# No stale placeholders or claim-inflating language.
forbidden=[
    "Stage 10 manuscript construction pending",
    "TODO",
    "FIXME",
    "the unique mixed equilibrium",
    "the complete mixed-equilibrium correspondence",
    "published Eq. (8) is wrong",
    "whole-model formal verification",
]
haystack=(all_tex+"\n"+cover).lower()
for phrase in forbidden:
    assert phrase.lower() not in haystack, f"forbidden/stale phrase found: {phrase}"

# Mandatory scope phrases.
assert "model-specific" in haystack
assert "unrestricted mixed-equilibrium uniqueness is not claimed" in haystack
assert "working-paper" in haystack
assert "proof-critical" in haystack

# Cover/title consistency.
title="Customer Recognition and Information Exchange with Kinked Price Competition: A Reassessment of the Model behind Shy and Stenbacka (2013)"
assert title in cover
assert title in (SUB/"title_page.md").read_text(encoding="utf-8")

# Declarations.
decl=(MAN/"sections/11_declarations.tex").read_text(encoding="utf-8").lower()
for phrase in [
    "credit authorship contribution statement",
    "funding",
    "competing interest",
    "data and code availability",
]:
    assert phrase in decl, f"missing declaration: {phrase}"

ai=(MAN/"sections/11_ai_declaration.tex").read_text(encoding="utf-8").lower()
assert "openai chatgpt" in ai
assert "full responsibility" in ai
assert "manuscript preparation process" in ai

print("stage14_submission_checks=PASS")
print("abstract_words",len(abstract_words))
print("keyword_count",len(keywords))
print("highlight_count",len(hl))
print("highlight_lengths",[len(x) for x in hl])
