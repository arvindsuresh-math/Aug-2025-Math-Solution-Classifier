def solve():
    """Index: 2894.
    Returns: the money Ian has left.
    """
    # L1
    hourly_rate = 18 # earn $18 per hour
    hours_worked = 8 # worked 8 hours
    total_earned = hourly_rate * hours_worked

    # L2
    spent_percentage_value = 50 # spent half the money / 50%
    percent_conversion_factor = 0.01 # WK
    money_spent = total_earned * spent_percentage_value * percent_conversion_factor

    # L3
    money_left = total_earned - money_spent

    # FA
    answer = money_left
    return answer