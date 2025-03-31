# Makefile for FastAPI project

.DEFAULT_GOAL:=help
.ONESHELL:
.EXPORT_ALL_VARIABLES:
MAKEFLAGS += --no-print-directory

# Variables
DOCKER_COMPOSE_DEV = docker-compose -f docker-compose.dev.yml
DOCKER_COMPOSE_PROD = docker-compose -f docker-compose.prod.yml
DOCKER_COMPOSE_TEST = docker-compose -f docker-compose.tests.yml
UV = uv
PRE_COMMIT = pre-commit
PYTEST = pytest
RUFF = ruff
UVICORN = uvicorn
PYRIGHT = pyright

# Help command
help:
	@echo "Available commands:"
	@echo "== Development Environment =="
	@echo "  up                 - Start the development environment using docker-compose"
	@echo "  down               - Stop the development environment"
	@echo "== Production Environment =="
	@echo "  prod               - Start the production environment using docker-compose.prod.yml"
	@echo "  down-prod          - Stop the production environment"
	@echo "== Dependencies =="
	@echo "  install-deps       - Install dependencies using uv"
	@echo "== Code Quality =="
	@echo "  check              - Run pre-commit checks"
	@echo "  check-install      - Install pre-commit hooks"
	@echo "  lint               - Perform linting on all files using ruff"
	@echo "  format             - Format all files using ruff format"
	@echo "  type-check         - Run static type checking using pyright"
	@echo "  pytest             - Run tests using pytest"
	@echo "  test               - Test the app (runs lint and format first)"
	@echo "== Application =="
	@echo "  start              - Start the app using uvicorn"
	@echo "== Miscellaneous =="
	@echo "  help               - Show this help message"

# Start the development environment
up:
	$(DOCKER_COMPOSE_DEV) up -d --build

# Stop the development environment
down:
	$(DOCKER_COMPOSE_DEV) down

# Start the production environment
prod:
	$(DOCKER_COMPOSE_PROD) up -d --build

# Stop the production environment
down-prod:
	$(DOCKER_COMPOSE_PROD) down

# Install dependencies using uv
install-deps:
	$(UV) sync --all-extras --dev

# Run pre-commit checks
check:
	$(UV) run $(PRE_COMMIT) run --all-files

# Install pre-commit hooks
pre-commit-install:
	$(PRE_COMMIT) install

# Perform linting on all files using ruff
lint:
	$(UV) run $(RUFF) check --fix .

# Format all files using ruff format
format:
	$(UV) run $(RUFF) format .

# Run static type checking using pyright
type-check:
	$(UV) run $(PYRIGHT)

# Run tests using pytest
pytest:
	$(DOCKER_COMPOSE_TEST) up --build --abort-on-container-exit
	$(DOCKER_COMPOSE_TEST) down

# Test the app (runs lint, format, and type-check first)
test: lint format type-check
	$(UV) run $(PYTEST) -v --durations=0 .

test-docker: lint format type-check pytest

# Start the app using uvicorn
start:
	$(UV) run $(UVICORN) src.main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: help up down up-prod down-prod migrate install-deps pre-commit pre-commit-install lint format type-check pytest test test-docker start create-env-unix create-env-windows init-unix init-windows dev
