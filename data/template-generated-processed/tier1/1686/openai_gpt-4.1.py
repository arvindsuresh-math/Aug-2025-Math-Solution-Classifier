def solve():
    """Index: 1686.
    Returns: the total number of hours Bob logs in a month.
    """
    # L1
    hours_per_day = 10 # Bob logs 10 hours of work in his office
    days_per_week = 5 # he works for five days a week
    weekly_hours = hours_per_day * days_per_week

    # L2
    weeks_per_month = 4 # a month with 4 weeks
    monthly_hours = weeks_per_month * weekly_hours

    # FA
    answer = monthly_hours
    return answer