from fastapi import FastAPI, Request

from app.services.store import store
from app.routers import auth as auth_router
from app.routers import accounts as accounts_router
from app.routers import transfer as transfer_router
from app.routers import transactions as transactions_router


TAGS_META = [
    {"name": "Authentication", "description": "JWT token generation and validation endpoints"},
    {"name": "Accounts", "description": "Account management and validation endpoints - Bonus features"},
    {"name": "Transfer", "description": "Fund transfer operations - Core challenge endpoint"},
    {"name": "transaction-controller", "description": "Transaction history endpoint (bonus)"},
]

app = FastAPI(
    title="🏦 Core Banking API (FastAPI)",
    description=(
        "Mock Banking API for Application Modernization Challenge\n\n"
        "- JWT Authentication (with scopes: enquiry, transfer)\n"
        "- Fund Transfers (core requirement)\n"
        "- Account Management (validation, balance inquiry)\n"
        "- Transaction History (bonus feature)\n"
    ),
    version="1.0.0",
    openapi_tags=TAGS_META,
)


@app.on_event("startup")
def init_state():
    store.init_defaults()


@app.get("/")
def read_root():
    return {"status": "ok"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/swagger-ui.html")
def swagger_alias():
    # Redirect to FastAPI's Swagger UI
    from fastapi.responses import RedirectResponse

    return RedirectResponse(url="/docs")


# Ensure in-memory store is initialized even if startup events aren't triggered (e.g., some tests)
@app.middleware("http")
async def ensure_store_initialized(request: Request, call_next):
    if not store.accounts:
        store.init_defaults()
    response = await call_next(request)
    return response


# Include routers
app.include_router(auth_router.router)
app.include_router(accounts_router.router)
app.include_router(transfer_router.router)
app.include_router(transactions_router.router)
