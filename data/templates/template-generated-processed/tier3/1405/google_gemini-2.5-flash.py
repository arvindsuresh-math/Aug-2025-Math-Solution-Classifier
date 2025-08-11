from fractions import Fraction

def solve():
    """Index: 1405.
    Returns: the total number of people who did not bring gifts.
    """
    # L1
    total_boys = 16 # Sixteen boys
    boys_gift_fraction_numerator = 3 # Three-fourths of the boys
    boys_gift_fraction_denominator = 4 # Three-fourths of the boys
    boys_brought_gifts = total_boys * Fraction(boys_gift_fraction_numerator, boys_gift_fraction_denominator)

    # L2
    boys_no_gifts = total_boys - boys_brought_gifts

    # L3
    total_girls = 14 # 14 girls
    girls_gift_fraction_numerator = 6 # 6/7 of the girls
    girls_gift_fraction_denominator = 7 # 6/7 of the girls
    girls_brought_gifts = total_girls * Fraction(girls_gift_fraction_numerator, girls_gift_fraction_denominator)

    # L4
    girls_no_gifts = total_girls - girls_brought_gifts

    # L5
    total_no_gifts = boys_no_gifts + girls_no_gifts

    # FA
    answer = total_no_gifts
    return answer