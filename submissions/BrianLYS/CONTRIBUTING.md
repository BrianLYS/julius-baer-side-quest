# Contributing

Thanks for your interest in improving the Core Banking API (FastAPI)!
This guide covers local setup, coding conventions, testing, and pull requests.

## Getting Started

- Prerequisites:
  - Python 3.11+
  - [uv](https://github.com/astral-sh/uv) (dependency manager)
- Setup:
  - Clone the repo and move into the project directory
  - Install deps: `uv sync` (dev tools: `uv sync --group dev`)
  - Optional: set `JWT_SECRET` for local tokens: `export JWT_SECRET="change-me"`

## Development Workflow

- Run the API (dev):
  - Autodiscovery: `uv run fastapi dev`
  - Explicit: `uv run fastapi dev app/main.py`
  - Match hackathon port: `uv run fastapi run app/main.py --port 8123 --host 0.0.0.0`
- Run tests:
  - `uv sync --group dev`
  - `uv run pytest -q`
- Lint/format (ruff):
  - Lint: `uv run ruff check .`
  - Format: `uv run ruff format .`

## Code Style & Architecture

- Python 3.11+, type hints everywhere. Prefer small, focused functions.
- FastAPI patterns:
  - Define request models in `app/models.py`.
  - Define response models in `app/schemas.py` and use `response_model`.
  - Document error responses via `responses={code: {"model": ErrorResponse}}`.
  - Keep endpoints in `app/routers/` (auth, accounts, transfer, transactions).
  - Put shared logic in `app/services/` and helpers in `app/utils/`.
  - Use auth dependencies from `app/dependencies/auth.py` for JWT access.
  - Avoid global state; use the `store` service for in-memory state.
- Behavior parity:
  - Preserve account rules (ACC1000–ACC1099 valid, ACC2000–ACC2049 inactive, others not found).
  - Don’t require auth for core endpoints unless specified (history requires auth).
  - Keep OpenAPI tags consistent with the spec.
- Documentation:
  - If you change any endpoint or behavior, update `README.md` and (if needed) examples.

## Commits & Pull Requests

- Branch naming: `feature/<short-desc>` or `fix/<short-desc>`.
- Commit style: concise, imperative subject. Conventional Commits optional but welcome.
- Keep PRs small and focused. Include:
  - What changed and why
  - Any behavioral differences
  - Tests covering new/changed logic
- Don’t bump versions or reformat the entire repo in feature PRs.

## Adding Endpoints

- Create a new file under `app/routers/` or extend an existing router.
- Add request models (models.py) and response models (schemas.py).
- Use dependency-injected auth (`get_optional_claims` or `require_claims`).
- Tag routes and add error responses metadata.
- Update `app/main.py` to include your router.
- Add tests in `tests/` using FastAPI `TestClient`.

## Security

- Never commit secrets. Use environment variables (e.g., `JWT_SECRET`).
- Keep JWT logic in `app/utils/jwt_utils.py` and auth dependencies in `app/dependencies/auth.py`.

## Questions

Open an issue or start a discussion in the repository. Thanks for contributing!

