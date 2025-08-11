def solve():
    """Index: 7317.
    Returns: the total number of days Mark has to wait.
    """
    # L1
    weeks_for_effectiveness = 2 # 2 weeks for the vaccine to be fully effective
    days_per_week = 7 # WK
    days_for_effectiveness = weeks_for_effectiveness * days_per_week

    # L2
    wait_first_appointment = 4 # 4 days for his first coronavirus vaccine appointment
    wait_second_appointment = 20 # 20 days for his second vaccine appointment
    total_wait_days = wait_first_appointment + wait_second_appointment + days_for_effectiveness

    # FA
    answer = total_wait_days
    return answer