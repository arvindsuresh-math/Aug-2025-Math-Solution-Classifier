from fractions import Fraction

def solve():
    """Index: 3000.
    Returns: the remaining length of the pole.
    """
    # L1
    shorter_percentage = Fraction(30, 100) # 30% shorter
    original_length = 20 # 20 meters long
    cut_away_length = shorter_percentage * original_length

    # L2
    remaining_length = original_length - cut_away_length

    # FA
    answer = remaining_length
    return answer