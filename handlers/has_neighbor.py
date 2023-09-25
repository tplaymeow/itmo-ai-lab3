import re

from swiplserver import PrologThread

pattern = re.compile(r"Does (?P<player_id>.+) have a neighbor\?")


def try_to_handle_has_neighbor(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    player_id = match.group("player_id")
    if player_id is None:
        return False

    result = prolog.query(f"has_neighbor({player_id})")
    print(
        f"{player_id} has neighbor"
        if result else
        f"{player_id} hasn't neighbor")
    return True
