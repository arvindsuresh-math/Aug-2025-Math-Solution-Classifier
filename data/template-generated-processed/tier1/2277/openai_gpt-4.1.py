def solve():
    """Index: 2277.
    Returns: the number of Davante's friends that are boys.
    """
    # L1
    multiplier = 2 # twice as many friends
    days_in_week = 7 # WK
    total_friends = multiplier * days_in_week

    # L2
    num_girls = 3 # 3 of his friends are girls
    num_boys = total_friends - num_girls

    # FA
    answer = num_boys
    return answer