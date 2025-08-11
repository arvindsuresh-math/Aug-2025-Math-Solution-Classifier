def solve():
    """Index: 3453.
    Returns: the total number of tomatoes Uncle Jerry reaped.
    """
    # L1
    tomatoes_yesterday = 120 # 120 tomatoes
    more_today = 50 # 50 more tomatoes than yesterday
    tomatoes_today = tomatoes_yesterday + more_today

    # L2
    total_tomatoes = tomatoes_yesterday + tomatoes_today

    # FA
    answer = total_tomatoes
    return answer