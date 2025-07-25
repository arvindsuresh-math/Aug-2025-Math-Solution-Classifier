def solve():
    """Index: 2229.
    Returns: the total money Zainab will earn after passing out flyers for 4 weeks.
    """
    # L1
    hourly_rate = 2 # $2 an hour
    hours_per_day = 4 # for 4 hours at a time
    earnings_per_day = hourly_rate * hours_per_day

    # L2
    days_per_week = 3 # on Monday, Wednesday, and Saturday each week
    earnings_per_week = earnings_per_day * days_per_week

    # L3
    num_weeks = 4 # for 4 weeks
    total_earnings = earnings_per_week * num_weeks

    # FA
    answer = total_earnings
    return answer