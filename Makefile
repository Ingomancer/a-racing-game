.venv: requirements.txt
	python -m venv .venv
	.venv/scripts/pip install -r requirements.txt

.PHONY: format
format:
	black *.py