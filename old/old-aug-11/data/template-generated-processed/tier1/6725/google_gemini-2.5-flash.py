def solve():
    """Index: 6725.
    Returns: the total earnings for the week.
    """
    # L1
    daily_earnings = 30 # $30 per day
    days_worked_per_week = 5 # 5 days a week
    weekly_base_earnings = daily_earnings * days_worked_per_week

    # L2
    overtime_earnings_per_shift = 15 # $15 more when she works a 2 hour overtime shift
    num_overtime_shifts = 3 # three overtime shifts this week
    total_overtime_earnings = overtime_earnings_per_shift * num_overtime_shifts

    # L3
    total_earnings_this_week = weekly_base_earnings + total_overtime_earnings

    # FA
    answer = total_earnings_this_week
    return answer