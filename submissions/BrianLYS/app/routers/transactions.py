from fastapi import APIRouter, Depends, Query

from app.dependencies.auth import require_claims
from app.services.store import store
from app.schemas import TransactionsHistoryResponse


router = APIRouter(tags=["transaction-controller"])


@router.get("/transactions/history", response_model=TransactionsHistoryResponse)
def get_transaction_history(
    claims: dict = Depends(require_claims),
    limit: int = Query(10, ge=1, le=20, description="Number of transactions to retrieve"),
):
    return {"transactions": store.transactions[:limit]}
