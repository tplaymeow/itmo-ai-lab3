import re

from swiplserver import PrologThread

pattern = re.compile(r"Can (?P<player_id>.+) buy (?P<object_id>.+)\?")


def try_to_handle_can_buy(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    player_id = match.group("player_id")
    object_id = match.group("object_id")
    if player_id is None or object_id is None:
        return False

    balance_result = prolog.query(f"balance({player_id},Balance)")
    price_result = prolog.query(f"object_price({object_id},Price)")
    has_owner_result = prolog.query(f"has_owner({object_id})")
    if balance_result is None or len(balance_result) == 0 or price_result is None or len(price_result) == 0:
        return False

    if has_owner_result:
        print(f"{object_id} has already bought")
    elif balance_result[0]["Balance"] < price_result[0]["Price"]:
        print(f"{player_id} have no enough money to buy {object_id}")
    else:
        print(f"{player_id} can buy {object_id}")
    return True
