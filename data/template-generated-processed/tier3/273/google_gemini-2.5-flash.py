from fractions import Fraction

def solve():
    """Index: 273.
    Returns: the length of the commercial after changes.
    """
    # L1
    shorten_percentage = Fraction(30, 100) # shorten the commercial by 30%
    commercial_length = 30 # a 30-second long commercial
    seconds_to_shorten = shorten_percentage * commercial_length

    # L2
    final_commercial_length = commercial_length - seconds_to_shorten

    # FA
    answer = final_commercial_length
    return answer