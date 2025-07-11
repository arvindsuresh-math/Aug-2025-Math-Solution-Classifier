def solve():
    """Index: 1331.
    Returns: the total number of hours Jane has exercised.
    """
    # L1
    hours_per_day_goal = 1 # 1 hour a day
    days_per_week_goal = 5 # 5 days a week
    weekly_exercise_hours = hours_per_day_goal * days_per_week_goal

    # L2
    num_weeks = 8 # for 8 weeks
    total_exercise_hours = weekly_exercise_hours * num_weeks

    # FA
    answer = total_exercise_hours
    return answer