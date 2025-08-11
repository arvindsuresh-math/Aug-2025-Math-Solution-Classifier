def solve():
    """Index: 1261.
    Returns: the number of cakes destroyed.
    """
    # L1
    initial_cakes = 12 # 12 angel food cakes
    fallen_divisor = 2 # knocked over half of the stack
    fallen_cakes = initial_cakes / fallen_divisor

    # L2
    destroyed_divisor = 2 # half of 6 fallen cakes were destroyed
    destroyed_cakes = fallen_cakes / destroyed_divisor

    # FA
    answer = destroyed_cakes
    return answer