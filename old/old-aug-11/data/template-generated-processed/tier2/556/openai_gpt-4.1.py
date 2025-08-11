def solve():
    """Index: 556.
    Returns: Roberto's current salary after two raises.
    """
    # L1
    starting_salary = 80000 # starting salary was $80,000
    first_raise_percent = 140 # 40% higher than his starting salary (100% + 40% = 140%)
    percent_factor = 0.01 # WK
    after_first_raise_salary = starting_salary * first_raise_percent * percent_factor

    # L2
    second_raise_percent = 120 # 20% raise (100% + 20% = 120%)
    current_salary = after_first_raise_salary * second_raise_percent * percent_factor

    # FA
    answer = current_salary
    return answer