from fractions import Fraction

def solve():
    """Index: 154.
    Returns: the total amount of money Ariella will have after two years.
    """
    # L1
    daniella_amount = 400 # Daniella has $400
    ariella_more_than_daniella = 200 # Ariella has $200 more
    ariella_initial_amount = daniella_amount + ariella_more_than_daniella

    # L2
    interest_rate_numerator = 10 # 10% per annum
    interest_rate_denominator = 100 # 10% per annum
    interest_rate = Fraction(interest_rate_numerator, interest_rate_denominator)
    interest_first_year = interest_rate * ariella_initial_amount

    # L3
    interest_second_year = interest_first_year # earns the same amount of interest
    total_interest = interest_first_year + interest_second_year

    # L4
    ariella_final_amount = ariella_initial_amount + total_interest

    # FA
    answer = ariella_final_amount
    return answer