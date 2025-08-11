def solve():
    """Index: 1796.
    Returns: the number of Dennis's rocks left.
    """
    # L1
    initial_rocks = 10 # Dennis collected 10 rocks
    eaten_divisor = 2 # his fish ate half of them
    rocks_after_eating = initial_rocks / eaten_divisor

    # L2
    spit_out_rocks = 2 # fish spit two out
    remaining_rocks = rocks_after_eating + spit_out_rocks

    # FA
    answer = remaining_rocks
    return answer