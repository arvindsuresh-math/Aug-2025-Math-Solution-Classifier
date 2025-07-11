def solve():
    """Index: 1790.
    Returns: the total number of infections during the second wave in 2 weeks.
    """
    # L1
    increase_factor = 4 # increased by four times more per day
    initial_daily_cases = 300 # 300 infections per day during the first wave
    additional_daily_cases = increase_factor * initial_daily_cases

    # L2
    current_daily_cases = additional_daily_cases + initial_daily_cases

    # L3
    num_weeks = 2 # in 2 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week
    total_infections_second_wave = total_days * current_daily_cases

    # FA
    answer = total_infections_second_wave
    return answer