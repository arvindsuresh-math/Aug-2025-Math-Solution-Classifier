def solve():
    """Index: 7336.
    Returns: the total miles Damien runs over three weeks.
    """
    # L1
    num_weeks = 3 # three weeks
    days_per_week_weekdays = 5 # weekdays only
    total_running_days = num_weeks * days_per_week_weekdays

    # L2
    miles_per_day = 5 # jogs 5 miles per day
    total_miles = miles_per_day * total_running_days

    # FA
    answer = total_miles
    return answer