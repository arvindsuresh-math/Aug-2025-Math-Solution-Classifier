def solve():
    """Index: 451.
    Returns: the number of light bulbs John has left after giving half of the remainder to a friend.
    """
    # L1
    initial_bulbs = 40 # John buys a box of 40 light bulbs
    used_bulbs = 16 # He uses 16 of them
    bulbs_left_after_use = initial_bulbs - used_bulbs

    # L2
    divisor = 2 # gives half of what is left
    bulbs_left_after_giving = bulbs_left_after_use / divisor

    # FA
    answer = bulbs_left_after_giving
    return answer