from fractions import Fraction

def solve():
    """Index: 5035.
    Returns: the total amount of money after 2 months, including interest.
    """
    # L1
    interest_rate_fraction = Fraction(10, 100) # 10 percent interest
    initial_investment = 300 # invest $300
    interest_month1 = interest_rate_fraction * initial_investment

    # L2
    total_after_month1 = initial_investment + interest_month1

    # L3
    interest_month2 = interest_rate_fraction * total_after_month1

    # L4
    total_after_month2 = total_after_month1 + interest_month2

    # FA
    answer = total_after_month2
    return answer