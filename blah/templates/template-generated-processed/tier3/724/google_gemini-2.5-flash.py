from fractions import Fraction

def solve():
    """Index: 724.
    Returns: half of Jenny's original amount of money.
    """
    # L1
    spent_fraction = Fraction(3, 7) # spending 3/7 of her money
    remaining_fraction = 1 - spent_fraction

    # L2
    money_left = 24 # $24 left
    numerator_of_remaining_fraction = remaining_fraction.numerator
    one_seventh_value = money_left / numerator_of_remaining_fraction

    # L3
    denominator_of_original_fraction = spent_fraction.denominator
    original_money = one_seventh_value * denominator_of_original_fraction

    # L4
    half_divisor = 2 # half of her original amount of money
    half_original_money = original_money / half_divisor

    # FA
    answer = half_original_money
    return answer