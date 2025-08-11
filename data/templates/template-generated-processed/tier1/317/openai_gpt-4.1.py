def solve():
    """Index: 317.
    Returns: the number of hours Madeline has left over in a week.
    """
    # L1
    homework_hours_per_day = 4 # 4 hours per day working on homework
    days_per_week = 7 # WK
    homework_hours_per_week = homework_hours_per_day * days_per_week

    # L2
    sleep_hours_per_day = 8 # 8 hours per day sleeping
    sleep_hours_per_week = sleep_hours_per_day * days_per_week

    # L3
    class_hours_per_week = 18 # 18 hours a week in class
    work_hours_per_week = 20 # 20 hours per week part-time work
    total_busy_hours = homework_hours_per_week + class_hours_per_week + sleep_hours_per_week + work_hours_per_week

    # L4
    hours_per_day = 24 # WK
    total_hours_per_week = days_per_week * hours_per_day

    # L5
    answer = total_hours_per_week - total_busy_hours
    return answer