from fractions import Fraction

def solve():
    """Index: 5232.
    Returns: the number of lavender candles Jill made.
    """
    # L1
    almond_candles = 10 # after making ten candles
    coconut_multiplier = Fraction(3, 2) # one and a half times as much coconut scent as almond scent
    coconut_candles = almond_candles * coconut_multiplier

    # L2
    lavender_multiplier = 2 # twice as many lavender candles
    lavender_candles = lavender_multiplier * coconut_candles

    # FA
    answer = lavender_candles
    return answer