VENV_DIR := .venv
PYTHON := python3
PIP := $(VENV_DIR)/bin/pip
UVICORN := $(VENV_DIR)/bin/uvicorn

create_venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"
	@echo "Run 'source $(VENV_DIR)/bin/activate' to activate it."

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

start:
	$(UVICORN) main:app --reload --reload-dir .

run:
	$(PYTHON) -m uvicorn main:app --reload --reload-dir .

activate:
	@echo "Run 'source $(VENV_DIR)/bin/activate' to activate the virtual environment."

clean:
	rm -rf $(VENV_DIR)

help:
	@echo "Usage:"
	@echo "  make install      Install dependencies in the virtual environment"
	@echo "  make start        Start the FastAPI app using uvicorn"
	@echo "  make run          Start the app explicitly with python -m uvicorn"
	@echo "  make activate     Instructions to activate the virtual environment"
	@echo "  make clean        Remove the virtual environment"
