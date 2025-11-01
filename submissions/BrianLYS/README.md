# Core Banking API (FastAPI)

## Quickstart

```bash
# Option 1: Autodiscovery (with app package)
uv run fastapi dev

# Option 2: Explicit target (file path)
uv run fastapi dev app/main.py

# Option 3: Explicit target (import path)
uv run fastapi dev --app app.main:app

# Match hackathon port locally (optional)
uv run fastapi run app/main.py --port 8123 --host 0.0.0.0
```

Optional: set JWT secret used to sign tokens

```bash
export JWT_SECRET="change-me"
```

Or use a local `.env` file:

```bash
cp .env.example .env
# export all vars in current shell
set -a; source .env; set +a
```

## Docker

```bash
docker build -t fastapi-new .
# Map standard challenge port 8123 to container port 80
docker run -p 8123:80 --env-file .env fastapi-new
```

## Project Structure

```
app/
  main.py                 # App factory, OpenAPI tags, router wiring
  models.py               # Request/input models
  schemas.py              # Response models (documented)
  config.py               # Minimal settings (env-based)
  services/
    store.py              # In-memory accounts + transactions store
  dependencies/
    auth.py               # Auth dependencies (require/optional claims)
  routers/
    auth.py               # /authToken, /auth/validate
    accounts.py           # /accounts, /accounts/validate/{id}, /accounts/balance/{id}
    transfer.py           # /transfer
    transactions.py       # /transactions/history
  utils/
    jwt_utils.py          # Minimal HS256 encode/decode + bearer parsing
    accounts.py           # Account ID validation helper
tests/
  test_api.py             # Basic integration tests (pytest + TestClient)
```

## Add new endpoint

```python
@app.get("/new-endpoint")
def new_endpoint():
    return {"message": "New endpoint"}
```

## Endpoints parity (hackathon)

- POST `/authToken` – issue JWT (`claim` query: `enquiry` or `transfer`)
- POST `/auth/validate` – validate `Authorization: Bearer <token>`
- POST `/transfer` – transfer funds (no auth required; bonus if JWT provided)
- GET `/accounts` – list valid accounts `ACC1000–ACC1099`
- GET `/accounts/validate/{id}` – validate and show active/inactive
- GET `/accounts/balance/{id}` – balance (inactive accounts return 400)
- GET `/transactions/history` – requires `Authorization` header
- GET `/swagger-ui.html` – redirects to FastAPI Swagger at `/docs`

See ROUTES.md for detailed route explanations and behavior notes.

### Example flow (cURL)

```bash
# 1) Swagger UI
curl -s localhost:8123/swagger-ui.html -I

# 2) Get a token (claim=transfer)
TOKEN=$(curl -s -X POST 'localhost:8123/authToken?claim=transfer' \
  -H 'content-type: application/json' -d '{"username":"alice","password":"any"}' | jq -r .token)

# 3) Validate token
curl -s -X POST 'localhost:8123/auth/validate' -H "Authorization: Bearer $TOKEN" | jq

# 4) List accounts and validate one
curl -s 'localhost:8123/accounts' | jq '.[0:3]'
curl -s 'localhost:8123/accounts/validate/ACC1000' | jq
curl -s 'localhost:8123/accounts/validate/ACC2000' | jq    # invalid range

# 5) Check balance
curl -s 'localhost:8123/accounts/balance/ACC1000' | jq

# 6) Transfer without auth (still works)
curl -s -X POST 'localhost:8123/transfer' -H 'content-type: application/json' \
  -d '{"fromAccount":"ACC1000","toAccount":"ACC1001","amount":100}' | jq

# 7) Transfer with auth (adds bonusPoints)
curl -s -X POST 'localhost:8123/transfer' \
  -H 'content-type: application/json' -H "Authorization: Bearer $TOKEN" \
  -d '{"fromAccount":"ACC1000","toAccount":"ACC1001","amount":5}' | jq

# 8) Transaction history (requires auth)
curl -s 'localhost:8123/transactions/history?limit=5' -H "Authorization: Bearer $TOKEN" | jq
```

## Tests

```bash
# Install dev deps (if not already in venv)
uv sync --group dev

# Run tests
uv run pytest -q
```


## Add new library

```bash
uv add fastapi-new
uv add ruff --dev
```

## Notes

- Account ranges: valid `ACC1000–ACC1099`, invalid/inactive `ACC2000–ACC2049`, others non-existent.
- Swagger alias: `/swagger-ui.html` redirects to `/docs` for convenience.
- Behavior matches Hackathon.md API; auth is required for history and optional elsewhere.
