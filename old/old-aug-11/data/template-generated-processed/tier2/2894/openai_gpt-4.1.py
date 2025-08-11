def solve():
    """Index: 2894.
    Returns: the amount of money Ian has left after spending half his earnings from online surveys.
    """
    # L1
    hourly_earning = 18 # $18 per hour doing surveys
    hours_worked = 8 # worked 8 hours doing surveys
    total_earned = hourly_earning * hours_worked

    # L2
    percent_spent_num = 50 # half the money he made
    percent_factor = 0.01 # WK
    amount_spent = total_earned * percent_spent_num * percent_factor

    # L3
    amount_left = total_earned - amount_spent

    # FA
    answer = amount_left
    return answer