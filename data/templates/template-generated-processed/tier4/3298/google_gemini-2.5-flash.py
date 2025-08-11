def solve():
    """Index: 3298.
    Returns: Bill's new win percentage.
    """
    # L1
    initial_games = 200 # 200 games of poker
    initial_win_percent_num = 63 # won 63% of them
    percent_factor = 0.01 # WK
    initial_wins = initial_games * initial_win_percent_num * percent_factor

    # L2
    new_games_played = 100 # plays 100 more games
    new_games_lost = 43 # loses 43 of them
    new_wins = new_games_played - new_games_lost

    # L3
    total_wins = new_wins + initial_wins

    # L4
    overall_total_games = initial_games + new_games_played

    # L5
    percent_multiplier = 100 # WK
    new_win_percentage = total_wins / overall_total_games * percent_multiplier

    # FA
    answer = new_win_percentage
    return answer