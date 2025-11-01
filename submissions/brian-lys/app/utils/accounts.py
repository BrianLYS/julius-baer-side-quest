import re


def validate_account_id(account_id: str) -> bool:
    return bool(re.fullmatch(r"ACC[0-9]{4}", account_id))

