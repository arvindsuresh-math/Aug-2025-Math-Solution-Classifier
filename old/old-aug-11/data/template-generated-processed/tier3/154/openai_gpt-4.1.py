from fractions import Fraction

def solve():
    """Index: 154.
    Returns: the total amount of money in Ariella's account after two years.
    """
    # L1
    daniella_amount = 400 # Daniella has $400
    difference = 200 # Ariella has $200 more
    ariella_amount = daniella_amount + difference

    # L2
    interest_rate = Fraction(10, 100) # 10% per annum
    first_year_interest = interest_rate * ariella_amount

    # L3
    second_year_interest = first_year_interest # simple interest, same amount each year
    total_interest = first_year_interest + second_year_interest

    # L4
    total_amount = ariella_amount + total_interest

    # FA
    answer = total_amount
    return answer