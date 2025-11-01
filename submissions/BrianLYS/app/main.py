import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

from app.routers import accounts as accounts_router
from app.routers import auth as auth_router
from app.routers import transactions as transactions_router
from app.routers import transfer as transfer_router
from app.services.store import store

TAGS_META = [
    {
        "name": "Authentication",
        "description": "JWT token generation and validation endpoints",
    },
    {
        "name": "Accounts",
        "description": "Account management and validation endpoints - Bonus features",
    },
    {
        "name": "Transfer",
        "description": "Fund transfer operations - Core challenge endpoint",
    },
    {
        "name": "transaction-controller",
        "description": "Transaction history endpoint (bonus)",
    },
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
    # Basic logging config
    logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
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


# CORS (use CORS_ORIGINS env var; defaults to allow all)
origins = [o.strip() for o in settings.cors_origins.split(",")] if settings.cors_origins != "*" else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global error handler for unexpected exceptions
@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logging.exception("Unhandled error: %s", exc)
    return JSONResponse(status_code=500, content={"status": "FAILED", "message": "Internal server error"})


# Include routers
app.include_router(auth_router.router)
app.include_router(accounts_router.router)
app.include_router(transfer_router.router)
app.include_router(transactions_router.router)
