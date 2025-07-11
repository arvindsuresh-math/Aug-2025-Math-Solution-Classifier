from fractions import Fraction

def solve():
    """Index: 474.
    Returns: the number of members who ordered orange juice.
    """
    # L1
    total_members = 30 # A club with 30 members
    lemon_juice_fraction = Fraction(2, 5) # Two-fifths of them ordered lemon juice
    lemon_juice_members = total_members * lemon_juice_fraction

    # L2
    remaining_members_after_lemon = total_members - lemon_juice_members

    # L3
    mango_juice_fraction_stated = Fraction(1, 3) # One-third of the remaining members ordered mango juice
    mango_juice_calculation_fraction = Fraction(2, 3) # 2/3 in the calculation
    mango_juice_members = remaining_members_after_lemon * mango_juice_calculation_fraction

    # L4
    orange_juice_members = remaining_members_after_lemon - mango_juice_members

    # FA
    answer = orange_juice_members
    return answer