from fractions import Fraction

def solve():
    """Index: 4971.
    Returns: the total number of points Callum earned.
    """
    # L1
    fraction_krishna_won = Fraction(3, 4) # 3/4 of the matches
    total_matches_played = 8 # eight matches
    krishna_wins = fraction_krishna_won * total_matches_played

    # L2
    callum_wins = total_matches_played - krishna_wins

    # L3
    points_per_round = 10 # earn 10 points
    callum_total_points = callum_wins * points_per_round

    # FA
    answer = callum_total_points
    return answer