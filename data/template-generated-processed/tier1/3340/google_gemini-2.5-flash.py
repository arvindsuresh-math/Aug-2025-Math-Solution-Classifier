def solve():
    """Index: 3340.
    Returns: the difference in points between their team and their opponent.
    """
    # L1
    sammy_score = 20 # Sammy scored 20 points
    gab_multiplier = 2 # twice as many as Sammy's score
    gab_score = sammy_score * gab_multiplier

    # L2
    cher_multiplier = 2 # twice as many as Gab's score
    cher_score = gab_score * cher_multiplier

    # L3
    team_score = sammy_score + gab_score + cher_score

    # L4
    opponent_score = 85 # their opponent scored 85 points
    point_difference = team_score - opponent_score

    # FA
    answer = point_difference
    return answer