.PHONY: verify tables manuscript clean formal

verify:
	python code/stage01_cleanroom_reproduction.py
	python code/stage04_no_information.py
	python code/stage04_global_price_certification.py
	python code/stage04a_primitive_evaluator.py
	python code/stage07_backward_induction.py
	python code/stage07_equilibrium_correspondence_audit.py
	python code/stage07_primitive_welfare.py
	python code/stage075a_portability_attacks.py

tables:
	python code/generate_tables.py

formal:
	lake build

manuscript: tables
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cd manuscript && bibtex main
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	rm -f manuscript/*.aux manuscript/*.bbl manuscript/*.blg manuscript/*.log manuscript/*.out manuscript/*.toc manuscript/*.pdf
