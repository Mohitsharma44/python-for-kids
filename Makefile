VENV=.venv
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

.PHONY: venv install dev run fmt lint clean

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

dev: install
	$(PIP) install -r requirements-dev.txt

run:
	$(PY) week01/gold_collector_game.py

fmt:
	$(VENV)/bin/black .
	$(VENV)/bin/isort .

lint:
	$(VENV)/bin/flake8

clean:
	rm -rf $(VENV)

