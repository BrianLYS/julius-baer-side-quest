import base64
import hashlib
import hmac
import json
from datetime import datetime, timezone
from typing import Optional

from app.config import settings
from fastapi import HTTPException


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _b64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def jwt_encode(payload: dict, secret: Optional[str] = None) -> str:
    header = {"alg": settings.jwt_alg, "typ": "JWT"}
    header_b64 = _b64url(json.dumps(header, separators=(",", ":")).encode())
    payload_b64 = _b64url(json.dumps(payload, separators=(",", ":")).encode())
    signing_input = f"{header_b64}.{payload_b64}".encode()
    signature = hmac.new(
        (secret or settings.jwt_secret).encode(), signing_input, hashlib.sha256
    ).digest()
    sig_b64 = _b64url(signature)
    return f"{header_b64}.{payload_b64}.{sig_b64}"


def jwt_decode(token: str, secret: Optional[str] = None) -> dict:
    try:
        header_b64, payload_b64, sig_b64 = token.split(".")
    except ValueError:
        raise HTTPException(
            status_code=401,
            detail={"status": "FAILED", "message": "Invalid token format"},
        )
    signing_input = f"{header_b64}.{payload_b64}".encode()
    expected_sig = hmac.new(
        (secret or settings.jwt_secret).encode(), signing_input, hashlib.sha256
    ).digest()
    try:
        provided_sig = _b64url_decode(sig_b64)
    except Exception:
        raise HTTPException(
            status_code=401,
            detail={"status": "FAILED", "message": "Invalid token signature"},
        )
    if not hmac.compare_digest(expected_sig, provided_sig):
        raise HTTPException(
            status_code=401,
            detail={"status": "FAILED", "message": "Signature verification failed"},
        )
    try:
        payload = json.loads(_b64url_decode(payload_b64))
    except Exception:
        raise HTTPException(
            status_code=401,
            detail={"status": "FAILED", "message": "Invalid token payload"},
        )
    # Expiry check
    now = int(datetime.now(timezone.utc).timestamp())
    if "exp" in payload and now >= int(payload["exp"]):
        raise HTTPException(
            status_code=401, detail={"status": "FAILED", "message": "Token expired"}
        )
    return payload


def bearer_token(auth_header: Optional[str]) -> Optional[str]:
    if not auth_header:
        return None
    parts = auth_header.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]
    return None
