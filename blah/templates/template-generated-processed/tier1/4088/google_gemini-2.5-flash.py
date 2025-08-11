def solve():
    """Index: 4088.
    Returns: the total amount Bill gets paid for a 50-hour workweek.
    """
    # L1
    hourly_rate_regular = 20 # Bill gets paid $20 every hour
    regular_hours_limit = 40 # up to a total of 40 hours
    paid_regular_hours = regular_hours_limit * hourly_rate_regular

    # L2
    double_multiplier = 2 # double that amount
    overtime_hourly_rate = hourly_rate_regular * double_multiplier

    # L3
    total_workweek_hours = 50 # for a 50-hour workweek
    remaining_hours = total_workweek_hours - regular_hours_limit
    paid_overtime_hours = remaining_hours * overtime_hourly_rate

    # L4
    total_paid = paid_regular_hours + paid_overtime_hours

    # FA
    answer = total_paid
    return answer