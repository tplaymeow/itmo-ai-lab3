import re

from swiplserver import PrologThread

pattern = re.compile(r"What distance between (?P<fists_player_id>.+) and (?P<second_player_id>.+)\?")


def try_to_handle_players_distance(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    fists_player_id = match.group("fists_player_id")
    second_player_id = match.group("second_player_id")
    if fists_player_id is None or second_player_id is None:
        return False

    result = prolog.query(f"players_distance({fists_player_id},{second_player_id},Distance)")
    if result is None or len(result) == 0:
        return False

    print(f"Distance between {fists_player_id} and {second_player_id} is {result[0]['Distance']}")
    return True
