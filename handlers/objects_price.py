import re

from swiplserver import PrologThread

pattern = re.compile(r"How much are all (?P<player_id>.+) objects price\?")


def try_to_handle_objects_price(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    player_id = match.group("player_id")
    if player_id is None:
        return False

    result = prolog.query(f"objects_price({player_id},Price)")
    if result is None or len(result) == 0:
        return False

    print(f"All {player_id} price is {result[0]['Price']}")
    return True
