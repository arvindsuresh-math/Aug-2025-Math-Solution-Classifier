def solve():
    """Index: 641.
    Returns: the number of dresses Alex can make.
    """
    # L1
    num_friends = 5 # all 5 of them
    silk_per_friend = 20 # 20 meters of silk each
    silk_given_to_friends = num_friends * silk_per_friend

    # L2
    initial_silk_storage = 600 # Alex has 600 meters of silk in storage
    silk_remaining = initial_silk_storage - silk_given_to_friends

    # L3
    silk_per_dress = 5 # Each dress needs 5 meters of silk
    num_dresses = silk_remaining / silk_per_dress

    # FA
    answer = num_dresses
    return answer