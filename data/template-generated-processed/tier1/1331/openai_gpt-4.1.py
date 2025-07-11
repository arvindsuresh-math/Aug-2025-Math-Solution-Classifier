def solve():
    """Index: 1331.
    Returns: the total number of hours Jane has exercised in 8 weeks if she hits her goal.
    """
    # L1
    hours_per_day = 1 # exercise 1 hour a day
    days_per_week = 5 # 5 days a week
    weekly_hours = hours_per_day * days_per_week

    # L2
    num_weeks = 8 # for 8 weeks
    total_hours = weekly_hours * num_weeks

    # FA
    answer = total_hours
    return answer