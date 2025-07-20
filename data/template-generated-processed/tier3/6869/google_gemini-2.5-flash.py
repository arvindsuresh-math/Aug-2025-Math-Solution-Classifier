def solve():
    """Index: 6869.
    Returns: the number of rounds William won.
    """
    # L1
    total_rounds = 15 # played 15 rounds of tic-tac-toe
    william_more_wins = 5 # William won 5 more rounds than Harry
    remaining_rounds = total_rounds - william_more_wins

    # L2
    num_players = 2 # There are 2 players
    rounds_per_player_equal_share = remaining_rounds / num_players

    # L3
    william_wins = rounds_per_player_equal_share + william_more_wins

    # FA
    answer = william_wins
    return answer