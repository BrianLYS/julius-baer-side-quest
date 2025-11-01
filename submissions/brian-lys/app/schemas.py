from typing import List, Optional
from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    status: str = Field(example="FAILED")
    message: str
    errors: Optional[List[str]] = None


class AuthTokenResponse(BaseModel):
    token: str
    username: str
    scope: str
    permissions: str
    expiresAt: str


class AuthValidateResponse(BaseModel):
    valid: bool
    username: Optional[str] = None
    scope: Optional[str] = None
    expiresAt: Optional[str] = None


class ValidateAccountResponse(BaseModel):
    accountId: str
    valid: bool
    active: bool
    invalidRange: bool


class BalanceResponse(BaseModel):
    accountId: str
    balance: float


class TransferResult(BaseModel):
    transactionId: str
    status: str
    message: str
    fromAccount: str
    toAccount: str
    amount: float
    availableBalance: Optional[float] = None
    requestedAmount: Optional[float] = None
    shortfall: Optional[float] = None
    bonusPoints: Optional[str] = None


class TransactionEntry(BaseModel):
    id: str
    result: TransferResult
    ts: str


class TransactionsHistoryResponse(BaseModel):
    transactions: List[TransactionEntry]

