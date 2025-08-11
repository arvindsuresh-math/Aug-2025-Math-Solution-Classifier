from fractions import Fraction

def solve():
    """Index: 1325.
    Returns: the total money Sally will make for the two months.
    """
    # L1
    last_month_earnings = 1000 # Sally earned $1000 at work last month
    percentage_factor_numerator = 110 # received a 10% raise (100% + 10%)
    percentage_factor_denominator = 100 # (110/100)
    this_month_earnings = last_month_earnings * Fraction(percentage_factor_numerator, percentage_factor_denominator)

    # L2
    total_earnings = last_month_earnings + this_month_earnings

    # FA
    answer = total_earnings
    return answer