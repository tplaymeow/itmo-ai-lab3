import re

from swiplserver import PrologThread

pattern = re.compile(r"What objects does (?P<player_id>.+) have\?")


def try_to_handle_all_objects(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    player_id = match.group("player_id")
    if player_id is None:
        return False

    result = prolog.query(f"player_ownership({player_id},Object)")
    if result is None or len(result) == 0:
        return False

    print(f"{player_id} has {', '.join([item['Object'] for item in result])}")
    return True
