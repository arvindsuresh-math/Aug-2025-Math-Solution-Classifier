def solve():
    """Index: 641.
    Returns: the number of dresses Alex can make for himself.
    """
    # L1
    num_friends = 5 # Alex gives all 5 of them
    silk_per_friend = 20 # 20 meters of silk each
    total_silk_given = num_friends * silk_per_friend

    # L2
    initial_silk = 600 # Alex has 600 meters of silk in storage
    silk_left = initial_silk - total_silk_given

    # L3
    silk_per_dress = 5 # Each dress needs 5 meters of silk
    dresses_alex_can_make = silk_left / silk_per_dress

    # FA
    answer = dresses_alex_can_make
    return answer