def solve():
    """Index: 2508.
    Returns: the total number of employees laid off.
    """
    # L1
    initial_employees = 1000 # 1000 employees
    layoff_percent_num = 10 # 10% of the remaining employees
    percent_factor = 0.01 # WK
    layoffs_round1 = initial_employees * layoff_percent_num * percent_factor

    # L2
    remaining_employees_after_round1 = initial_employees - layoffs_round1

    # L3
    layoffs_round2 = remaining_employees_after_round1 * layoff_percent_num * percent_factor

    # L4
    remaining_employees_after_round2 = remaining_employees_after_round1 - layoffs_round2

    # L5
    layoffs_round3 = remaining_employees_after_round2 * layoff_percent_num * percent_factor

    # L6
    total_layoffs = layoffs_round1 + layoffs_round2 + layoffs_round3

    # FA
    answer = total_layoffs
    return answer