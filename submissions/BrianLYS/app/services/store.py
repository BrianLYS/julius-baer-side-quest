from typing import Dict, List, Set


class Store:
    def __init__(self) -> None:
        # Valid active accounts
        self.accounts: Dict[str, float] = {}
        # Inactive/invalid range
        self.inactive_accounts: Set[str] = set()
        # Recent transactions
        self.transactions: List[dict] = []

    def init_defaults(self) -> None:
        self.accounts = {f"ACC{1000 + i}": 1000.0 for i in range(100)}
        self.inactive_accounts = {f"ACC{2000 + i}" for i in range(50)}
        self.transactions = []


store = Store()
