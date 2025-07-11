def solve():
    """Index: 2229.
    Returns: the total amount of money Zainab will earn after 4 weeks.
    """
    # L1
    hourly_wage = 2 # $2 an hour
    hours_per_day = 4 # 4 hours at a time
    daily_earnings = hourly_wage * hours_per_day

    # L2
    days_per_week = 3 # Monday, Wednesday, and Saturday each week
    weekly_earnings = daily_earnings * days_per_week

    # L3
    num_weeks = 4 # after passing out flyers for 4 weeks
    total_earnings = weekly_earnings * num_weeks

    # FA
    answer = total_earnings
    return answer