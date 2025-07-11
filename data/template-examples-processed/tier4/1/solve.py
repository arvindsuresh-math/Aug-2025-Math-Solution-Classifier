def solve():
    """Index: 1.
    Returns: how much Weng earned from babysitting.
    """
    # L1
    hourly_rate = 12 # earns $12 an hour
    minutes_per_hour = 60 # WK
    per_minute_rate = hourly_rate / minutes_per_hour

    # L2
    minutes_worked = 50 # did 50 minutes of babysitting
    total_earned = per_minute_rate * minutes_worked

    # FA
    answer = total_earned
    return answer