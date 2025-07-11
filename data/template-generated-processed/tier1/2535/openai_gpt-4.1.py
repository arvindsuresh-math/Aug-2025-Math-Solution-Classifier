def solve():
    """Index: 2535.
    Returns: the total amount of money Jamie will have earned after 6 weeks of delivering flyers.
    """
    # L1
    days_per_week = 2 # delivers flyers 2 days each week
    hours_per_day = 3 # takes her 3 hours each time
    hours_per_week = days_per_week * hours_per_day

    # L2
    num_weeks = 6 # after delivering flyers for 6 weeks
    total_hours = hours_per_week * num_weeks

    # L3
    hourly_rate = 10 # earns $10 an hour
    total_earned = total_hours * hourly_rate

    # FA
    answer = total_earned
    return answer