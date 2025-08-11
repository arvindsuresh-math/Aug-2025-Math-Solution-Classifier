def solve():
    """Index: 4068.
    Returns: the total time to free all friends.
    """
    # L1
    cheap_handcuffs_time = 6 # 6 minutes
    expensive_handcuffs_time = 8 # 8 minutes
    time_per_friend = cheap_handcuffs_time + expensive_handcuffs_time

    # L2
    num_friends = 3 # three of her friends
    total_time = time_per_friend * num_friends

    # FA
    answer = total_time
    return answer