from fractions import Fraction

def solve():
    """Index: 3345.
    Returns: the total prize money won by Rica's group.
    """
    # L1
    spent_fraction = Fraction(1, 5) # spent 1/5 of it
    remaining_amount_rica = 300 # is now left with $300
    initial_fraction_whole = 1 # WK
    remaining_fraction_rica = initial_fraction_whole - spent_fraction

    # L2
    numerator_remaining_fraction = 4 # WK
    value_of_one_fifth = remaining_amount_rica / numerator_remaining_fraction

    # L3
    denominator_spent_fraction = 5 # WK
    ricas_total_prize_money = value_of_one_fifth * denominator_spent_fraction
    ricas_share_fraction = Fraction(3, 8) # She got 3/8 of the prize money

    # L4
    ricas_share_numerator = 3 # WK
    one_eighth_fraction = Fraction(1, 8) # WK
    value_of_one_eighth = ricas_total_prize_money / ricas_share_numerator

    # L5
    total_prize_denominator = 8 # WK
    total_prize_money = value_of_one_eighth * total_prize_denominator

    # FA
    answer = total_prize_money
    return answer