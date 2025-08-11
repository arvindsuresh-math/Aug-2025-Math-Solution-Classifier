def solve():
    """Index: 2324.
    Returns: the total amount of money Isabella will have earned after 7 weeks of babysitting.
    """
    # L1
    hourly_rate = 5 # earns $5 an hour babysitting
    hours_per_day = 5 # babysits 5 hours every day
    daily_earnings = hourly_rate * hours_per_day

    # L2
    days_per_week = 6 # 6 afternoons a week
    weekly_earnings = daily_earnings * days_per_week

    # L3
    num_weeks = 7 # after babysitting for 7 weeks
    total_earnings = weekly_earnings * num_weeks

    # FA
    answer = total_earnings
    return answer