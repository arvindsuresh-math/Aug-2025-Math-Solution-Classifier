from fractions import Fraction

def solve():
    """Index: 4425.
    Returns: the total amount Mary Anne spends on sparkling water every year.
    """
    # L1
    fraction_consumed_per_night_decimal = 0.2 # 1/5 of a bottle of sparkling water
    fraction_consumed_per_night_fraction = Fraction(1, 5) # 1/5 of a bottle of sparkling water
    days_in_year = 365 # WK
    total_bottles_consumed_yearly = fraction_consumed_per_night_decimal * days_in_year

    # L2
    cost_per_bottle = 2.00 # $2.00
    total_annual_spend = cost_per_bottle * total_bottles_consumed_yearly

    # FA
    answer = total_annual_spend
    return answer