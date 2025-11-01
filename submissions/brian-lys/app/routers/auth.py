from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Query, Depends

from app.models import AuthRequest
from app.utils.jwt_utils import jwt_encode
from app.dependencies.auth import require_claims
from app.schemas import AuthTokenResponse, AuthValidateResponse


router = APIRouter(tags=["Authentication"])


@router.post("/authToken", response_model=AuthTokenResponse)
def get_auth_token(body: AuthRequest, claim: str = Query("enquiry", description="Claim/scope for the token: 'enquiry' or 'transfer'")):
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(hours=1)
    payload = {
        "sub": body.username,
        "scope": claim,
        "iat": int(now.timestamp()),
        "exp": int(expires_at.timestamp()),
    }
    token = jwt_encode(payload)
    return {
        "token": token,
        "username": body.username,
        "scope": claim,
        "permissions": claim,
        "expiresAt": expires_at.isoformat().replace("+00:00", "Z"),
    }


@router.post("/auth/validate", response_model=AuthValidateResponse)
def validate_jwt(claims: dict = Depends(require_claims)):
    exp = datetime.fromtimestamp(int(claims["exp"]), tz=timezone.utc) if "exp" in claims else None
    return {
        "valid": True,
        "username": claims.get("sub"),
        "scope": claims.get("scope"),
        "expiresAt": exp.isoformat().replace("+00:00", "Z") if exp else None,
    }
