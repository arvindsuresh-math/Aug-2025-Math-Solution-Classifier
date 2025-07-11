def solve():
    """Index: 556.
    Returns: Roberto's current salary.
    """
    # L1
    starting_salary = 80000 # starting salary was $80,000
    first_raise_percent_text = 40 # 40% higher
    first_raise_factor_percent = 140 # 140%
    percent_to_decimal_factor = 0.01 # WK
    salary_after_first_raise = starting_salary * first_raise_factor_percent * percent_to_decimal_factor

    # L2
    second_raise_percent_text = 20 # 20% raise
    second_raise_factor_percent = 120 # 120%
    current_salary = salary_after_first_raise * second_raise_factor_percent * percent_to_decimal_factor

    # FA
    answer = current_salary
    return answer