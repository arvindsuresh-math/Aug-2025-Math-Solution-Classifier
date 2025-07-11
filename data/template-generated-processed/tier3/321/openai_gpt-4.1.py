from fractions import Fraction

def solve():
    """Index: 321.
    Returns: Mike's current salary.
    """
    # L1
    mike_multiplier = 10 # Mike earned 10 times more money than Fred
    fred_salary = 1000 # Fred's salary then was $1000
    mike_extra = mike_multiplier * fred_salary

    # L2
    mike_past_salary = mike_extra + fred_salary

    # L3
    increase_percent = Fraction(40, 100) # salary has increased by 40 percent
    mike_increase = increase_percent * mike_past_salary

    # L4
    mike_current_salary = mike_past_salary + mike_increase

    # FA
    answer = mike_current_salary
    return answer