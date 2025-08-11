def solve():
    """Index: 7315.
    Returns: the total number of roses Bella received.
    """
    # L1
    num_dozen_parents = 2 # 2 dozen roses from her parents
    dozen = 12 # WK
    roses_from_parents = num_dozen_parents * dozen

    # L2
    roses_per_friend = 2 # 2 roses from each of her 10 dancer friends
    num_friends = 10 # 10 dancer friends
    roses_from_friends = roses_per_friend * num_friends

    # L3
    total_roses = roses_from_parents + roses_from_friends

    # FA
    answer = total_roses
    return answer