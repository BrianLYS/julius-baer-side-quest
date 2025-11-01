from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def get_token(scope="transfer"):
    r = client.post(
        f"/authToken?claim={scope}", json={"username": "alice", "password": "any"}
    )
    assert r.status_code == 200, r.text
    return r.json()["token"]


def test_health_endpoints():
    assert client.get("/").json()["status"] == "ok"
    assert client.get("/ping").json()["message"] == "pong"


def test_accounts_listing_and_validation():
    r = client.get("/accounts")
    assert r.status_code == 200
    accounts = r.json()
    assert len(accounts) == 100

    r = client.get("/accounts/validate/ACC1000")
    data = r.json()
    assert data["valid"] is True and data["active"] is True

    r = client.get("/accounts/validate/ACC2000")
    data = r.json()
    assert data["invalidRange"] is True and data["active"] is False


def test_auth_and_history():
    token = get_token()
    r = client.post("/auth/validate", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["valid"] is True

    r = client.get(
        "/transactions/history", headers={"Authorization": f"Bearer {token}"}
    )
    assert r.status_code == 200
    assert "transactions" in r.json()


def test_transfer_success_and_insufficient_funds():
    # success
    r = client.post(
        "/transfer",
        json={"fromAccount": "ACC1000", "toAccount": "ACC1001", "amount": 10.0},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "SUCCESS"

    # insufficient funds (request a huge amount)
    r = client.post(
        "/transfer",
        json={"fromAccount": "ACC1000", "toAccount": "ACC1001", "amount": 10_000_000.0},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "FAILED"
