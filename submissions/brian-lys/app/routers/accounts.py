from typing import List, Optional

from fastapi import APIRouter, Header, HTTPException

from app.models import Account
from app.schemas import ValidateAccountResponse, BalanceResponse, ErrorResponse
from app.services.store import store
from app.utils.accounts import validate_account_id


router = APIRouter(tags=["Accounts"])


def _classify_account(account_id: str):
    if not validate_account_id(account_id):
        return {"formatValid": False, "exists": False, "active": False, "invalid": False}
    if account_id in store.accounts:
        return {"formatValid": True, "exists": True, "active": True, "invalid": False}
    if account_id in store.inactive_accounts:
        return {"formatValid": True, "exists": True, "active": False, "invalid": True}
    return {"formatValid": True, "exists": False, "active": False, "invalid": False}


@router.get("/accounts", response_model=List[Account])
def get_all_accounts(Authorization: Optional[str] = Header(None)):
    # Auth is optional; ignoring header but accepting it for compatibility
    return [Account(id=acc_id, balance=bal) for acc_id, bal in store.accounts.items()]


@router.get("/accounts/validate/{accountId}", response_model=ValidateAccountResponse)
def validate_account(accountId: str, Authorization: Optional[str] = Header(None)):
    c = _classify_account(accountId)
    return {
        "accountId": accountId,
        "valid": c["formatValid"] and c["exists"],
        "active": c["active"],
        "invalidRange": c["invalid"],
    }


@router.get(
    "/accounts/balance/{accountId}",
    response_model=BalanceResponse,
    responses={400: {"model": ErrorResponse}, 404: {"model": ErrorResponse}},
)
def get_account_balance(accountId: str, Authorization: Optional[str] = Header(None)):
    if not validate_account_id(accountId):
        raise HTTPException(status_code=400, detail={
            "status": "FAILED",
            "message": "Invalid account format",
            "errors": ["accountId must match pattern ACC[0-9]{4}"]
        })
    if accountId in store.inactive_accounts:
        raise HTTPException(status_code=400, detail={"status": "FAILED", "message": "Account inactive"})
    if accountId not in store.accounts:
        raise HTTPException(status_code=404, detail={"status": "FAILED", "message": "Account not found"})
    return {"accountId": accountId, "balance": store.accounts[accountId]}
