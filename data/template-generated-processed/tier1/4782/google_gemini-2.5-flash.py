def solve():
    """Index: 4782.
    Returns: the number of games Henry had at first.
    """
    # L1
    games_given_to_neil = 6 # gave six of them to Neil
    neil_initial_games = 7 # Neil had 7 games at first
    neil_games_after_henry_gives = games_given_to_neil + neil_initial_games

    # L2
    henry_multiplier = 4 # 4 times more games than Neil
    henry_games_now = neil_games_after_henry_gives * henry_multiplier

    # L3
    henry_initial_games = henry_games_now + games_given_to_neil

    # FA
    answer = henry_initial_games
    return answer