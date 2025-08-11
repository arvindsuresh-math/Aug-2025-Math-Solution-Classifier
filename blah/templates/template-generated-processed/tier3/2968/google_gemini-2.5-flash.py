from fractions import Fraction

def solve():
    """Index: 2968.
    Returns: the number of months John needs to work to make the same amount of money Karen does in 3 months.
    """
    # L1
    john_salary_per_month = 3000 # John makes $3000 per month
    john_salary_fraction_of_karen = Fraction(3, 4) # Jon makes 3/4's the salary that Karen makes
    karen_salary_per_month = john_salary_per_month / john_salary_fraction_of_karen

    # L2
    karen_months_to_calculate = 3 # Karen does in 3 months
    karen_total_salary_in_three_months = karen_salary_per_month * karen_months_to_calculate

    # L3
    john_months_to_match_karen = karen_total_salary_in_three_months / john_salary_per_month

    # FA
    answer = john_months_to_match_karen
    return answer