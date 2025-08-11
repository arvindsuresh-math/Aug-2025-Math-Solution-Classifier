def solve():
    """Index: 6373.
    Returns: the total amount Tim made that week.
    """
    # L1
    num_days_initial = 6 # for the first 6 days
    visitors_per_day = 100 # 100 visitors a day
    initial_visits = num_days_initial * visitors_per_day

    # L2
    multiplier_last_day = 2 # twice as many visitors
    last_day_visits = initial_visits * multiplier_last_day

    # L3
    total_visits = last_day_visits + initial_visits

    # L4
    earnings_per_visit = 0.01 # $.01 per visit
    total_earnings = total_visits * earnings_per_visit

    # FA
    answer = total_earnings
    return answer