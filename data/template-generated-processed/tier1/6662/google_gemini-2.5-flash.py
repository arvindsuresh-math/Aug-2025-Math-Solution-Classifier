def solve():
    """Index: 6662.
    Returns: the total amount Queenie will receive.
    """
    # L1
    daily_rate = 150 # $150 a day
    num_days_worked = 5 # working 5 days
    earnings_from_days = daily_rate * num_days_worked

    # L2
    overtime_rate_per_hour = 5 # $5 per hour as overtime pay
    overtime_hours = 4 # 4 hours overtime
    overtime_earnings = overtime_rate_per_hour * overtime_hours

    # L3
    total_earnings = earnings_from_days + overtime_earnings

    # FA
    answer = total_earnings
    return answer