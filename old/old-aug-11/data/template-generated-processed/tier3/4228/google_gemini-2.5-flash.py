from fractions import Fraction

def solve():
    """Index: 4228.
    Returns: the total amount Martha saved at the end of the week.
    """
    # L1
    daily_allowance = 12 # daily allowance of $12
    half_fraction = Fraction(1, 2) # save half of this amount
    half_saved_amount = half_fraction * daily_allowance

    # L2
    days_in_week = 7 # WK
    exception_days = 1 # one day
    days_saved_half = days_in_week - exception_days

    # L3
    total_saved_half_days = half_saved_amount * days_saved_half

    # L4
    quarter_fraction = Fraction(1, 4) # saved only a quarter of this amount
    quarter_saved_amount = quarter_fraction * daily_allowance

    # L5
    total_savings = quarter_saved_amount + total_saved_half_days

    # FA
    answer = total_savings
    return answer