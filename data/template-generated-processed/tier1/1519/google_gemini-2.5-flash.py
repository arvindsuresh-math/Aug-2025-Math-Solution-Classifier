def solve():
    """Index: 1519.
    Returns: the total money Sandy earned on Friday, Saturday, and Sunday.
    """
    # L1
    friday_hours = 10 # 10 hours on Friday
    saturday_hours = 6 # 6 hours on Saturday alone
    sunday_hours = 14 # 14 hours on Sunday
    total_hours_worked = friday_hours + saturday_hours + sunday_hours

    # L2
    hourly_rate = 15 # $15 per hour
    total_earnings = total_hours_worked * hourly_rate

    # FA
    answer = total_earnings
    return answer