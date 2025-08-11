def solve():
    """Index: 451.
    Returns: the number of light bulbs John has left.
    """
    # L1
    initial_bulbs = 40 # a box of 40 light bulbs
    bulbs_used = 16 # He uses 16 of them
    bulbs_after_use = initial_bulbs - bulbs_used

    # L2
    divisor_for_friend = 2 # gives half of what is left
    bulbs_left = bulbs_after_use / divisor_for_friend

    # FA
    answer = bulbs_left
    return answer