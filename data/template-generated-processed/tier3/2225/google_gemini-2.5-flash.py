from fractions import Fraction

def solve():
    """Index: 2225.
    Returns: Bob's current salary.
    """
    # L1
    marios_salary_this_year = 4000 # Mario's salary increased by 40% to $4000 this year
    multiplier_for_bobs_last_year_salary = 3 # three times Mario's salary this year
    bobs_salary_last_year = multiplier_for_bobs_last_year_salary * marios_salary_this_year

    # L2
    increase_numerator = 20 # 20% more than his salary last year
    increase_denominator = 100 # 20% more than his salary last year
    salary_increase_percentage = Fraction(increase_numerator, increase_denominator)
    bobs_salary_increase = salary_increase_percentage * bobs_salary_last_year

    # L3
    bobs_current_salary = bobs_salary_last_year + bobs_salary_increase

    # FA
    answer = bobs_current_salary
    return answer