from fractions import Fraction

def solve():
    """Index: 321.
    Returns: Mike's current salary.
    """
    # L1
    fred_salary = 1000 # Fred's salary then was $1000
    mike_multiplier = 10 # 10 times more money
    mike_earned_more_than_fred = mike_multiplier * fred_salary

    # L2
    mike_salary_five_months_ago = mike_earned_more_than_fred + fred_salary

    # L3
    salary_increase_percentage = Fraction(40, 100) # increased by 40 percent
    salary_increase_amount = salary_increase_percentage * mike_salary_five_months_ago

    # L4
    mike_current_salary = mike_salary_five_months_ago + salary_increase_amount

    # FA
    answer = mike_current_salary
    return answer