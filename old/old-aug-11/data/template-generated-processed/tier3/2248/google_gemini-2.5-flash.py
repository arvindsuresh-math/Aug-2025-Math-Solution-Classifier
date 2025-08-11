from fractions import Fraction

def solve():
    """Index: 2248.
    Returns: the total number of wins in the three competitions.
    """
    # L1
    first_competition_wins = 40 # won 40 games in their last competition
    second_competition_multiplier = Fraction(5, 8) # won 5/8 times as many games
    second_competition_wins = second_competition_multiplier * first_competition_wins

    # L2
    third_competition_wins = second_competition_wins + first_competition_wins

    # L3
    sum_first_two_competitions = first_competition_wins + second_competition_wins
    total_wins = sum_first_two_competitions + third_competition_wins

    # FA
    answer = total_wins
    return answer