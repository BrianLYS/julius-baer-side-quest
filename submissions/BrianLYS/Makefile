.PHONY: install dev run test lint format fix docker-build docker-run

VENV_BIN := .venv/bin

install:
	uv sync

dev: install
	$(VENV_BIN)/fastapi dev app/main.py

run: install
	$(VENV_BIN)/fastapi run app/main.py --port $${PORT:-8123} --host 0.0.0.0

test: install
	$(VENV_BIN)/pytest -q

lint: install
	$(VENV_BIN)/ruff check .

format: install
	$(VENV_BIN)/ruff format .

fix: install
	$(VENV_BIN)/ruff check --fix . && $(VENV_BIN)/ruff format .

docker-build:
	docker build -t fastapi-new .

docker-run:
	docker run --rm -p $${PORT:-8123}:80 --env-file .env fastapi-new
