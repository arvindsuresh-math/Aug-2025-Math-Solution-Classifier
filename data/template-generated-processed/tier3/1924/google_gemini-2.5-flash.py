from fractions import Fraction

def solve():
    """Index: 1924.
    Returns: the total points Vlad scored.
    """
    # L1
    points_per_win = 5 # 5 points for every win
    total_rounds = 30 # After playing 30 rounds
    total_possible_points = points_per_win * total_rounds

    # L2
    taro_fraction = Fraction(3, 5) # 3/5 of the total points scored
    taro_fraction_of_total_points = taro_fraction * total_possible_points

    # L3
    taro_points_less = 4 # 4 points less
    taro_score = taro_fraction_of_total_points - taro_points_less

    # L4
    vlad_score = total_possible_points - taro_score

    # FA
    answer = vlad_score
    return answer