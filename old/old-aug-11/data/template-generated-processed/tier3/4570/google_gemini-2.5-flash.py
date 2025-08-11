from fractions import Fraction

def solve():
    """Index: 4570.
    Returns: the amount of money Tom has left to finish the month.
    """
    # L1
    initial_allowance = 12 # $12 allowance per month
    first_week_fraction = Fraction(1, 3) # a third of it
    spent_first_week = initial_allowance * first_week_fraction

    # L2
    money_after_first_week = initial_allowance - spent_first_week

    # L3
    second_week_fraction = Fraction(1, 4) # a quarter of what he has left
    spent_second_week = money_after_first_week * second_week_fraction

    # L4
    money_left_end_month = money_after_first_week - spent_second_week

    # FA
    answer = money_left_end_month
    return answer