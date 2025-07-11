def solve():
    """Index: 2299.
    Returns: the percentage of games Archibald has won.
    """
    # L1
    archibald_wins = 12 # Archibald has won 12 games
    brother_wins = 18 # his brother has won 18
    total_games = archibald_wins + brother_wins

    # L2
    archibald_proportion = archibald_wins / total_games

    # L3
    percent_multiplier = 100 # WK
    archibald_percent = archibald_proportion * percent_multiplier

    # FA
    answer = archibald_percent
    return answer