import re

from swiplserver import PrologThread

pattern = re.compile(r"Where should (?P<player_id>.+) go\?")


def try_to_handle_where_should_go(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    player_id = match.group("player_id")
    if player_id is None:
        return False

    balance_result = prolog.query(f"balance({player_id},Balance)")
    ownership_result = prolog.query(f"player_ownership({player_id},Object)")
    ownership_cat_result = prolog.query(f"player_ownership({player_id},Object), object_category(Object,Category)")
    position_result = prolog.query(f"player_position({player_id},Position)")
    if (balance_result is None or len(balance_result) == 0 or
            position_result is None or len(position_result) == 0):
        return False

    balance = balance_result[0]["Balance"]
    position = position_result[0]["Position"]
    ownership = {item["Object"] for item in ownership_result}
    ownership_cat = {item["Category"] for item in ownership_cat_result}

    result = (position + 7) % 16

    for pos in range(position + 1, position + 7):
        pos = pos % 16

        obj_result = prolog.query(f"object_position(Object,{pos})")
        if not obj_result or len(obj_result) == 0:
            continue

        obj = obj_result[0]["Object"]
        if obj in ownership:
            continue

        has_owner_result = prolog.query(f"has_owner({obj})")
        if has_owner_result:
            continue

        obj_price_result = prolog.query(f"object_price({obj},Price)")
        if obj_price_result is None or len(obj_price_result) == 0:
            continue

        obj_price = obj_price_result[0]["Price"]
        if balance < obj_price:
            continue

        obj_cat_result = prolog.query(f"object_category({obj},Category)")
        if obj_cat_result is None or len(obj_cat_result) == 0:
            continue

        obj_cat = obj_cat_result[0]["Category"]
        if obj_cat in ownership_cat:
            result = pos

    print(f"{player_id} should go to {result}")

    return True
