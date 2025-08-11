def solve():
    """Index: 6500.
    Returns: the total number of matches Sam won.
    """
    # L1
    first_matches_total = 100 # first 100 matches
    first_win_percentage_decimal = 0.5 # won 50% of matches
    first_matches_won = first_matches_total * first_win_percentage_decimal

    # L2
    next_matches_total = 100 # next 100 games
    next_win_percentage_decimal = 0.6 # won 60% of matches
    next_matches_won = next_matches_total * next_win_percentage_decimal

    # L3
    total_matches_won = first_matches_won + next_matches_won

    # FA
    answer = total_matches_won
    return answer