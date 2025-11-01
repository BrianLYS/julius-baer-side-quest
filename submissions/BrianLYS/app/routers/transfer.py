import uuid
from datetime import datetime, timezone
from typing import Optional

from app.dependencies.auth import get_optional_claims
from app.models import TransferRequest
from app.schemas import ErrorResponse, TransferResult
from app.services.store import store
from app.utils.accounts import validate_account_id
from fastapi import APIRouter, Depends, Header, HTTPException

router = APIRouter(tags=["Transfer"])


@router.post(
    "/transfer",
    response_model=TransferResult,
    responses={400: {"model": ErrorResponse}, 404: {"model": ErrorResponse}},
)
def transfer_funds(
    req: TransferRequest,
    Authorization: Optional[str] = Header(None, description="Bearer token (optional)"),
    claims: Optional[dict] = Depends(get_optional_claims),
):
    # Validate account formats
    errors = []
    if not validate_account_id(req.fromAccount):
        errors.append("fromAccount must match pattern ACC[0-9]{4}")
    if not validate_account_id(req.toAccount):
        errors.append("toAccount must match pattern ACC[0-9]{4}")
    if errors:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "FAILED",
                "message": "Invalid account format",
                "errors": errors,
            },
        )

    # Inactive range check
    if (
        req.fromAccount in store.inactive_accounts
        or req.toAccount in store.inactive_accounts
    ):
        raise HTTPException(
            status_code=400, detail={"status": "FAILED", "message": "Account inactive"}
        )

    if req.fromAccount not in store.accounts or req.toAccount not in store.accounts:
        raise HTTPException(
            status_code=404, detail={"status": "FAILED", "message": "Account not found"}
        )

    tx_id = str(uuid.uuid4())
    # Insufficient funds check
    if store.accounts[req.fromAccount] < req.amount:
        result = {
            "transactionId": tx_id,
            "status": "FAILED",
            "message": "Insufficient funds",
            "fromAccount": req.fromAccount,
            "toAccount": req.toAccount,
            "amount": req.amount,
            "availableBalance": store.accounts[req.fromAccount],
            "requestedAmount": req.amount,
            "shortfall": round(req.amount - store.accounts[req.fromAccount], 2),
        }
        store.transactions.insert(
            0,
            {
                "id": tx_id,
                "result": result,
                "ts": datetime.now(timezone.utc).isoformat(),
            },
        )
        store.transactions = store.transactions[:50]
        return result

    # Perform transfer
    store.accounts[req.fromAccount] -= req.amount
    store.accounts[req.toAccount] += req.amount
    result = {
        "transactionId": tx_id,
        "status": "SUCCESS",
        "message": "Transfer completed successfully",
        "fromAccount": req.fromAccount,
        "toAccount": req.toAccount,
        "amount": req.amount,
    }
    # Bonus flag if a valid token was provided
    if claims and claims.get("scope") in {"transfer", "enquiry"}:
        result["bonusPoints"] = "🌟 JWT Authentication Bonus!"

    store.transactions.insert(
        0, {"id": tx_id, "result": result, "ts": datetime.now(timezone.utc).isoformat()}
    )
    store.transactions = store.transactions[:50]
    return result
