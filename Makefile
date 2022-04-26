VENV_DIR=.venv
ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV_DIR)/Scripts
else
	VENV_BIN=$(VENV_DIR)/bin
endif

.PHONY: venv
venv: requirements

.PHONY: cleanvenv
cleanvenv:
	rm -rf $(VENV_DIR)

$(VENV_DIR): 
	python -m venv $(VENV_DIR)

.PHONY: requirements
requirements: $(VENV_DIR) requirements.txt
	$(VENV_BIN)/pip install -r requirements.txt

.PHONY: format
format:
	$(VENV_BIN)/black *.py

.PHONY: run
run:
	$(VENV_BIN)/python racing.py