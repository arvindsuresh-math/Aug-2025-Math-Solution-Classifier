def solve():
    """Index: 5213.
    Returns: the speed gained per week in mph.
    """
    # L1
    initial_speed_mph = 80 # 80 miles per hour
    speed_increase_percent_decimal = 0.2 # 20% faster
    speed_gained_total_mph = initial_speed_mph * speed_increase_percent_decimal

    # L2
    num_training_sessions = 4 # 4 times
    weeks_per_session = 4 # 4 weeks each time
    total_training_weeks = num_training_sessions * weeks_per_session

    # L3
    speed_gained_per_week_mph = speed_gained_total_mph / total_training_weeks

    # FA
    answer = speed_gained_per_week_mph
    return answer