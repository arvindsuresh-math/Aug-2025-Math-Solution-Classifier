def solve():
    """Index: 2324.
    Returns: the total money Isabella will have earned after babysitting for 7 weeks.
    """
    # L1
    hourly_rate = 5 # $5 an hour
    hours_per_day = 5 # 5 hours every day
    daily_earnings = hourly_rate * hours_per_day

    # L2
    afternoons_per_week = 6 # 6 afternoons a week
    weekly_earnings = daily_earnings * afternoons_per_week

    # L3
    num_weeks = 7 # 7 weeks
    total_earnings = weekly_earnings * num_weeks

    # FA
    answer = total_earnings
    return answer