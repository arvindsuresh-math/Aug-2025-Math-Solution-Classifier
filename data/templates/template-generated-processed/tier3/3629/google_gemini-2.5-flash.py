from fractions import Fraction

def solve():
    """Index: 3629.
    Returns: the total number of red or white roses.
    """
    # L1
    total_roses = 80 # 80 roses in her garden
    red_fraction_numerator = 3 # Three-fourths of her roses are red
    red_fraction_denominator = 4 # Three-fourths of her roses are red
    red_roses = total_roses * Fraction(red_fraction_numerator, red_fraction_denominator)

    # L2
    non_red_roses = total_roses - red_roses

    # L3
    yellow_fraction_numerator = 1 # one-fourth of the remaining are yellow
    yellow_fraction_denominator = 4 # one-fourth of the remaining are yellow
    yellow_roses = non_red_roses * Fraction(yellow_fraction_numerator, yellow_fraction_denominator)

    # L4
    white_roses = non_red_roses - yellow_roses

    # L5
    red_or_white_roses = red_roses + white_roses

    # FA
    answer = red_or_white_roses
    return answer