def solve():
    """Index: 6093.
    Returns: the number of squats performed the day after tomorrow.
    """
    # L1
    squats_yesterday = 30 # I did 30 squats
    increase_per_day = 5 # increase my number of squats by 5 more than the previous day
    squats_today = squats_yesterday + increase_per_day

    # L2
    squats_tomorrow = squats_today + increase_per_day

    # L3
    squats_day_after_tomorrow = squats_tomorrow + increase_per_day

    # FA
    answer = squats_day_after_tomorrow
    return answer