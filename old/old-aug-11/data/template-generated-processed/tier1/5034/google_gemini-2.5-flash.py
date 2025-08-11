def solve():
    """Index: 5034.
    Returns: the amount of free time Jackie has per day.
    """
    # L1
    hours_working = 8 # 8 hours working
    hours_sleeping = 8 # 8 hours of sleep
    hours_exercise = 3 # 3 hours of exercise
    total_spent_hours = hours_working + hours_sleeping + hours_exercise

    # L2
    hours_in_day = 24 # WK
    free_time = hours_in_day - total_spent_hours

    # FA
    answer = free_time
    return answer