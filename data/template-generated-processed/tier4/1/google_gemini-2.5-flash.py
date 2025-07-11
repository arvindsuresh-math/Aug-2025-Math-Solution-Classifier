def solve():
    """Index: 1.
    Returns: the amount Weng earned for babysitting.
    """
    # L1
    hourly_rate = 12 # Weng earns $12 an hour
    minutes_per_hour = 60 # WK
    rate_per_minute = hourly_rate / minutes_per_hour

    # L2
    minutes_worked = 50 # 50 minutes of babysitting
    total_earnings = rate_per_minute * minutes_worked

    # FA
    answer = total_earnings
    return answer