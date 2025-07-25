def solve():
    """Index: 5391.
    Returns: the number of games Reggie has lost.
    """
    # L1
    friend_initial_marbles = 100 # friend arrives with 100 marbles
    reggie_final_marbles = 90 # Reggie has 90 marbles
    marbles_lost = friend_initial_marbles - reggie_final_marbles

    # L2
    marbles_bet_per_game = 10 # they bet ten marbles
    games_lost = marbles_lost / marbles_bet_per_game

    # FA
    answer = games_lost
    return answer