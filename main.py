import sys

from swiplserver import PrologMQI, create_posix_path, PrologThread

from handlers.all_objects import try_to_handle_all_objects
from handlers.can_buy import try_to_handle_can_buy
from handlers.distance_to_object import try_to_handle_distance_to_object
from handlers.has_neighbor import try_to_handle_has_neighbor
from handlers.neighbor_players import try_to_handle_neighbor_players
from handlers.objects_price import try_to_handle_objects_price
from handlers.players_distance import try_to_handle_players_distance
from handlers.where_should_go import try_to_handle_where_should_go


def run(prolog: PrologThread) -> None:
    while True:
        try:
            message = input()
            handled = (
                    try_to_handle_distance_to_object(prolog, message)
                    or try_to_handle_players_distance(prolog, message)
                    or try_to_handle_neighbor_players(prolog, message)
                    or try_to_handle_has_neighbor(prolog, message)
                    or try_to_handle_objects_price(prolog, message)
                    or try_to_handle_all_objects(prolog, message)
                    or try_to_handle_can_buy(prolog, message)
                    or try_to_handle_where_should_go(prolog_thread, message))
            if not handled:
                print("Incorrect input")
        except EOFError:
            break


if __name__ == "__main__":
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            path = create_posix_path(sys.argv[1])
            prolog_thread.query(f"consult(\"{path}\")")
            run(prolog_thread)
