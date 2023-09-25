import re

from swiplserver import PrologThread

pattern = re.compile(r"What distance from (?P<player_id>.+) to (?P<object_id>.+)\?")


def try_to_handle_distance_to_object(prolog: PrologThread, message: str) -> bool:
    match = re.match(pattern, message)
    if match is None:
        return False

    player_id = match.group("player_id")
    object_id = match.group("object_id")
    if player_id is None or object_id is None:
        return False

    result = prolog.query(f"distance_to_object({player_id},{object_id},Distance)")
    if result is None or len(result) == 0:
        return False

    print(f"Distance between {player_id} and {object_id} is {result[0]['Distance']}")
    return True
