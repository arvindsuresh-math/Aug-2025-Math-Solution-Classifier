def solve():
    """Index: 2508.
    Returns: the total number of employees laid off after three rounds.
    """
    # L1
    initial_employees = 1000 # 1000 employees
    layoff_percent_num = 10 # 10% of the remaining employees
    percent_factor = 0.01 # WK
    first_round_layoffs = initial_employees * layoff_percent_num * percent_factor

    # L2
    after_first_round = initial_employees - first_round_layoffs

    # L3
    second_round_layoffs = after_first_round * layoff_percent_num * percent_factor

    # L4
    after_second_round = after_first_round - second_round_layoffs

    # L5
    third_round_layoffs = after_second_round * layoff_percent_num * percent_factor

    # L6
    total_laid_off = first_round_layoffs + second_round_layoffs + third_round_layoffs

    # FA
    answer = total_laid_off
    return answer