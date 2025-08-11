def solve():
    """Index: 5955.
    Returns: the total number of pills John takes in a week.
    """
    # L1
    hours_in_a_day = 24 # WK
    pill_frequency_hours = 6 # every 6 hours
    pills_per_day = hours_in_a_day / pill_frequency_hours

    # L2
    days_in_a_week = 7 # WK
    pills_per_week = pills_per_day * days_in_a_week

    # FA
    answer = pills_per_week
    return answer