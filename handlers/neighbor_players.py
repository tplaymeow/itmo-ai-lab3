import re

from swiplserver import PrologThread

pattern = re.compile(r"Are (?P<first_player_id>.+) and (?P<second_player_id>.+) neighbors\?")


def try_to_handle_neighbor_players(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    first_player_id = match.group("first_player_id")
    second_player_id = match.group("second_player_id")
    if first_player_id is None or second_player_id is None:
        return False

    result = prolog.query(f"neighbor_players({first_player_id},{second_player_id})")
    print(
        f"{first_player_id} and {second_player_id} are neighbors"
        if result else
        f"{first_player_id} and {second_player_id} aren't neighbors")
    return True
