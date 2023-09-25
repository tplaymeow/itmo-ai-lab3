balance(timur, 600).
balance(roman, 500).
balance(vadim, 400).
balance(gleb, 300).

player_position(timur, 0).
player_position(roman, 1).
player_position(vadim, 15).
player_position(gleb, 10).

object_category(four_seasons, hotel).
object_category(holiday_inn, hotel).
object_category(marriott, hotel).
object_category(mercedes, car).
object_category(bmw, car).
object_category(ford, car).
object_category(tinkoff, bank).
object_category(sber, bank).
object_category(alfa, bank).
object_category(vk, it).
object_category(yandex, it).
object_category(microsoft, it).

object_position(four_seasons, 1).
object_position(holiday_inn, 2).
object_position(marriott, 3).
object_position(mercedes, 5).
object_position(bmw, 6).
object_position(ford, 7).
object_position(tinkoff, 9).
object_position(sber, 10).
object_position(alfa, 11).
object_position(vk, 13).
object_position(yandex, 14).
object_position(microsoft, 15).

object_price(four_seasons, 100).
object_price(holiday_inn, 200).
object_price(marriott, 300).
object_price(mercedes, 100).
object_price(bmw, 200).
object_price(ford, 300).
object_price(tinkoff, 100).
object_price(sber, 200).
object_price(alfa, 300).
object_price(vk, 100).
object_price(yandex, 200).
object_price(microsoft, 300).

player_ownership(timur, holiday_inn).
player_ownership(roman, bmw).
player_ownership(vadim, sber).
player_ownership(gleb, vk).
player_ownership(gleb, yandex).

has_owner(Object) :-
    player_ownership(_, Object).

distance_to_object(Player, Object, Distance) :-
    player_position(Player, PlayerPos),
    object_position(Object, ObjectPos),
    Distance is (ObjectPos - PlayerPos) mod 16.

players_distance(Player1, Player2, Distance) :-
    player_position(Player1, Player1Pos),
    player_position(Player2, Player2Pos),
    Distance is min((Player2Pos - Player1Pos) mod 16, (Player1Pos - Player2Pos) mod 16).

neighbor_players(Player1, Player2) :-
    players_distance(Player1, Player2, 1).

has_neighbor(Player1) :-
    neighbor_players(Player1, _).

list_sum([],0).
list_sum([Head|Tail], TotalSum):-
    list_sum(Tail, Sum1),
    TotalSum is Head+Sum1.

objects_price(Player, Price) :-
    findall(Object, player_ownership(Player, Object), Objects),
    maplist(object_price, Objects, Prices),
    list_sum(Prices, Price).