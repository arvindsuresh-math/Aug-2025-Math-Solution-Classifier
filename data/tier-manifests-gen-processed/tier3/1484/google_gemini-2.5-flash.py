from fractions import Fraction

def solve():
    """Index: 1484.
    Returns: the initial amount of money Lucy had.
    """
    # L1
    remaining_money_after_spending = 15 # only left with $15
    fraction_spent_remainder = Fraction(1, 4) # spent one-fourth of the remainder
    fraction_of_money_left_after_spending = 1 - fraction_spent_remainder

    # L2
    value_of_one_quarter = remaining_money_after_spending / fraction_of_money_left_after_spending.numerator

    # L3
    money_left_after_loss = value_of_one_quarter * fraction_of_money_left_after_spending.denominator

    # L4
    fraction_lost_initial = Fraction(1, 3) # lost one-third of her money
    fraction_of_initial_money_remaining = 1 - fraction_lost_initial

    # L5
    value_of_one_third = money_left_after_loss / fraction_of_initial_money_remaining.numerator

    # L6
    initial_money = value_of_one_third * fraction_of_initial_money_remaining.denominator

    # FA
    answer = initial_money
    return answer