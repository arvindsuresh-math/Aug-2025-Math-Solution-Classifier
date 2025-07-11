def solve():
    """Index: 1519.
    Returns: the total amount of money Sandy earned on Friday, Saturday, and Sunday.
    """
    # L1
    hours_friday = 10 # worked 10 hours on Friday
    hours_saturday = 6 # 6 hours on Saturday
    hours_sunday = 14 # 14 hours on Sunday
    total_hours = hours_friday + hours_saturday + hours_sunday

    # L2
    hourly_rate = 15 # earns $15 per hour
    total_earnings = total_hours * hourly_rate

    # FA
    answer = total_earnings
    return answer