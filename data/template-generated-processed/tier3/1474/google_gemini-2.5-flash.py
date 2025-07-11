def solve():
    """Index: 1474.
    Returns: the average number of hours of television watched per week.
    """
    # L1
    last_week_hours = 10 # 10 hours of television last week
    week_before_hours = 8 # 8 hours of television
    next_week_hours = 12 # 12 hours of television next week
    total_hours = last_week_hours + week_before_hours + next_week_hours

    # L2
    number_of_weeks = 3 # WK
    average_hours = total_hours / number_of_weeks

    # FA
    answer = average_hours
    return answer