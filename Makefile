ifeq ($(OS),Windows_NT)
	VENV=.venv/Scripts
else
	VENV=.venv/bin
endif

.PHONY: venv
venv: requirements

.venv: 
	python -m venv .venv
	
.PHONY: requirements
requirements: .venv requirements.txt
	$(VENV)/pip install -r requirements.txt

.PHONY: format
format:
	$(VENV)/black *.py

.PHONY: run
run:
	$(VENV)/python racing.py