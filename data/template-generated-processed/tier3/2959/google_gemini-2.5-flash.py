def solve():
    """Index: 2959.
    Returns: the number of friends who received pebbles.
    """
    # L1
    num_dozens = 3 # three dozens of pebbles
    pebbles_per_dozen = 12 # WK
    total_pebbles = num_dozens * pebbles_per_dozen

    # L2
    pebbles_per_friend = 4 # Each of her friends got 4 pebbles
    num_friends = total_pebbles / pebbles_per_friend

    # FA
    answer = num_friends
    return answer