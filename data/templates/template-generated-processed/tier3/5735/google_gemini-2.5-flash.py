from fractions import Fraction

def solve():
    """Index: 5735.
    Returns: the difference in total entry fees collected.
    """
    # L1
    stadium_capacity = 2000 # capacity of 2000 people
    entry_fee_per_person = 20 # paid $20 in entry fees
    full_stadium_fees = stadium_capacity * entry_fee_per_person

    # L2
    fraction_full_numerator = 3 # 3/4 of the total capacity
    fraction_full_denominator = 4 # 3/4 of the total capacity
    people_at_three_quarters_full = Fraction(fraction_full_numerator, fraction_full_denominator) * stadium_capacity

    # L3
    fees_at_three_quarters_full = people_at_three_quarters_full * entry_fee_per_person

    # L4
    difference_in_fees = full_stadium_fees - fees_at_three_quarters_full

    # FA
    answer = difference_in_fees
    return answer