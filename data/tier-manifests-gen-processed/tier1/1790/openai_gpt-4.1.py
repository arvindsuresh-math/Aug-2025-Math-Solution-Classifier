def solve():
    """Index: 1790.
    Returns: the total number of infections during the second wave in 2 weeks.
    """
    # L1
    increase_factor = 4 # increased by four times more per day
    first_wave_per_day = 300 # 300 infections per day during the first wave
    additional_per_day = increase_factor * first_wave_per_day

    # L2
    second_wave_per_day = additional_per_day + first_wave_per_day

    # L3
    days_in_two_weeks = 14 # 2 weeks with 14 days
    total_infections = days_in_two_weeks * second_wave_per_day

    # FA
    answer = total_infections
    return answer