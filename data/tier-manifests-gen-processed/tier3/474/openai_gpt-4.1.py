from fractions import Fraction

def solve():
    """Index: 474.
    Returns: the number of members who ordered orange juice.
    """
    # L1
    total_members = 30 # 30 members
    lemon_fraction_numerator = 2 # Two-fifths of them ordered lemon juice
    lemon_fraction_denominator = 5 # Two-fifths of them ordered lemon juice
    lemon_fraction = Fraction(lemon_fraction_numerator, lemon_fraction_denominator)
    lemon_juice_members = total_members * lemon_fraction

    # L2
    remaining_after_lemon = total_members - lemon_juice_members

    # L3
    mango_fraction_numerator = 1 # One-third of the remaining members ordered mango juice
    mango_fraction_denominator = 3 # One-third of the remaining members ordered mango juice
    mango_fraction = Fraction(mango_fraction_numerator, mango_fraction_denominator)
    mango_juice_members = remaining_after_lemon * mango_fraction

    # L4
    orange_juice_members = remaining_after_lemon - mango_juice_members

    # FA
    answer = orange_juice_members
    return answer