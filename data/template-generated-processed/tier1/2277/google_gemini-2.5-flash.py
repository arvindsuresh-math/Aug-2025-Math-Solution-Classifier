def solve():
    """Index: 2277.
    Returns: the number of friends Davante has that are boys.
    """
    # L1
    multiplier = 2 # twice as many friends
    days_in_week = 7 # WK
    total_friends = multiplier * days_in_week

    # L2
    girl_friends = 3 # 3 of his friends are girls
    boy_friends = total_friends - girl_friends

    # FA
    answer = boy_friends
    return answer