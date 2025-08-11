def solve():
    """Index: 2299.
    Returns: the percentage of games Archibald has won.
    """
    # L1
    archibald_games_won = 12 # Archibald has won 12 games
    brother_games_won = 18 # his brother has won 18
    total_games_played = archibald_games_won + brother_games_won

    # L2
    archibald_proportion_won = archibald_games_won / total_games_played

    # L3
    percent_multiplier = 100 # WK
    archibald_percentage_won = archibald_proportion_won * percent_multiplier

    # FA
    answer = archibald_percentage_won
    return answer