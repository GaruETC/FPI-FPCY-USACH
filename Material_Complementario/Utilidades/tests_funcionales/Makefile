VENV := .venv
PYTHON := python
ifeq ($(OS),Windows_NT)
	BIN := $(VENV)\Scripts
	ACTIVATE := $(BIN)\activate

	RM := rmdir /s /q
	MKDIR := mkdir
	SEP := \\
else
	BIN := $(VENV)/bin
	ACTIVATE := . $(BIN)/activate

	RM := rm -rf
	MKDIR := mkdir -p
	SEP := /
endif

.PHONY: install run clean

.DEFAULT_GOAL := run

$(VENV):
	@$(PYTHON) -m venv $(VENV)

install: $(VENV)
	@$(BIN)/pip install -q -r requirements.txt

run: $(VENV)
	@$(BIN)/python main.py $(ARGS)

clean:
	@$(RM) $(VENV)
