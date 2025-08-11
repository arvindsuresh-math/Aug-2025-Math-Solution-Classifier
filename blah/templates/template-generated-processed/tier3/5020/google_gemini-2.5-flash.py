from fractions import Fraction

def solve():
    """Index: 5020.
    Returns: the amount Alice will save this month.
    """
    # L1
    sales_value = 2500 # $2500 worth of gadgets
    commission_rate_numerator = 2 # 2% commission
    commission_rate_denominator = 100 # 2% commission
    commission_amount = sales_value * Fraction(commission_rate_numerator, commission_rate_denominator)

    # L2
    basic_salary = 240 # monthly basic salary of $240
    total_earnings = basic_salary + commission_amount

    # L3
    savings_rate_numerator = 10 # 10% of her total earnings
    savings_rate_denominator = 100 # 10% of her total earnings
    savings_amount = total_earnings * Fraction(savings_rate_numerator, savings_rate_denominator)

    # FA
    answer = savings_amount
    return answer