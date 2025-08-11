from fractions import Fraction

def solve():
    """Index: 273.
    Returns: the length in seconds of the commercial after shortening.
    """
    # L1
    shorten_percentage = Fraction(30, 100) # shorten the commercial by 30%
    original_length = 30 # 30-second long commercial
    seconds_shorter = shorten_percentage * original_length

    # L2
    shortened_length = original_length - seconds_shorter

    # FA
    answer = shortened_length
    return answer