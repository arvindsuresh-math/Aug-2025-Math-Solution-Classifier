def solve():
    """Index: 1497.
    Returns: the number of games Neil had at first.
    """
    # L1
    henry_initial_games = 33 # Henry had 33 games
    games_given_to_neil = 5 # he gave five of them to Neil
    henry_games_after_giving = henry_initial_games - games_given_to_neil

    # L2
    times_more_than_neil = 4 # Henry has 4 times more games than Neil
    neil_games_now = henry_games_after_giving / times_more_than_neil

    # L3
    neil_games_at_first = neil_games_now - games_given_to_neil

    # FA
    answer = neil_games_at_first
    return answer