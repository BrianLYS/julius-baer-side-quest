from pydantic import BaseModel, Field


class TransferRequest(BaseModel):
    fromAccount: str = Field(..., example="ACC1000")
    toAccount: str = Field(..., example="ACC1001")
    amount: float = Field(..., gt=0, example=150.0)


class AuthRequest(BaseModel):
    username: str = Field(..., example="alice")
    password: str = Field(..., example="password123")


class Account(BaseModel):
    id: str
    balance: float
