# API Routes Overview

This document summarizes all routes, their purpose, auth requirements, inputs, outputs, and key notes.

## Authentication

- `POST /authToken`
  - Purpose: Issue a JWT for clients.
  - Auth: Not required.
  - Request: JSON body `{ "username": string, "password": string }`, query `claim` (`enquiry` default, or `transfer`).
  - Response 200: `{ token, username, scope, permissions, expiresAt }`.
  - Notes: HS256 JWT signed with `JWT_SECRET`; expires in 1 hour.

- `POST /auth/validate`
  - Purpose: Validate and introspect a JWT.
  - Auth: Required (header `Authorization: Bearer <token>`).
  - Request: No body.
  - Response 200: `{ valid: true, username, scope, expiresAt }`.
  - Errors: 401 if missing/invalid/expired token.

## Transfer

- `POST /transfer`
  - Purpose: Core transfer operation between two accounts.
  - Auth: Optional (bonusPoints added if valid token provided).
  - Request: JSON body `{ fromAccount, toAccount, amount }`.
  - Response 200 (success): `{ transactionId, status: "SUCCESS", message, fromAccount, toAccount, amount, bonusPoints? }`.
  - Response 200 (insufficient funds): `{ transactionId, status: "FAILED", message: "Insufficient funds", fromAccount, toAccount, amount, availableBalance, requestedAmount, shortfall }`.
  - Errors: 400 (invalid format or inactive account), 404 (account not found).
  - Notes: Stores last 50 transactions; account IDs must match `ACC[0-9]{4}`.

## Accounts

- `GET /accounts`
  - Purpose: List all valid active accounts.
  - Auth: Optional.
  - Response 200: Array of `{ id, balance }`. Contains 100 accounts `ACC1000–ACC1099`.

- `GET /accounts/validate/{accountId}`
  - Purpose: Validate account ID and status.
  - Auth: Optional.
  - Response 200: `{ accountId, valid, active, invalidRange }`.
  - Notes:
    - Valid active: `ACC1000–ACC1099` → `valid=true, active=true`.
    - Inactive/invalid range: `ACC2000–ACC2049` → `valid=true, active=false, invalidRange=true`.
    - Non-existent: others → `valid=false` (or `exists=false`).

- `GET /accounts/balance/{accountId}`
  - Purpose: Retrieve balance for an account.
  - Auth: Optional.
  - Response 200: `{ accountId, balance }`.
  - Errors: 400 (bad format or inactive), 404 (not found).

## Transactions

- `GET /transactions/history`
  - Purpose: Recent transaction history (bonus endpoint).
  - Auth: Required (header `Authorization: Bearer <token>`).
  - Query: `limit` (default 10, max 20).
  - Response 200: `{ transactions: [ { id, result: TransferResult, ts } ] }`.
  - Errors: 401 if missing/invalid token.

## Health & Docs

- `GET /` — Simple health/status: `{ status: "ok" }`.
- `GET /ping` — Liveness: `{ message: "pong" }`.
- `GET /swagger-ui.html` — Redirects to FastAPI Swagger UI at `/docs`.

## Behavior Notes

- Account ranges:
  - Valid active: `ACC1000–ACC1099` (can send/receive funds).
  - Inactive/invalid: `ACC2000–ACC2049` (validation shows inactive; transfers/balance return errors).
  - Others: not found.
- Auth:
  - Only `/transactions/history` and `/auth/validate` require auth.
  - Other endpoints accept `Authorization` optionally.
- Tokens:
  - JWT HS256 with `sub`, `scope`, `iat`, `exp`. Signed using `JWT_SECRET`.

