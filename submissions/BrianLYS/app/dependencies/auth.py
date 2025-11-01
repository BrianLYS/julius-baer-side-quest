from datetime import datetime, timezone
from typing import Optional

from fastapi import Header, HTTPException

from app.utils.jwt_utils import bearer_token, jwt_decode


def get_optional_claims(Authorization: Optional[str] = Header(None)) -> Optional[dict]:
    token = bearer_token(Authorization)
    if not token:
        return None
    try:
        return jwt_decode(token)
    except HTTPException:
        # Optional: ignore invalid tokens; treat as unauthenticated
        return None


def require_claims(Authorization: Optional[str] = Header(None)) -> dict:
    token = bearer_token(Authorization)
    if not token:
        raise HTTPException(status_code=401, detail={"status": "FAILED", "message": "Authorization token required"})
    return jwt_decode(token)

