def solve():
    """Index: 5950.
    Returns: the total number of necklaces Latch caught.
    """
    # L1
    boudreaux_necklaces = 12 # Boudreaux caught twelve necklaces
    half_divisor = 2 # half as many necklaces
    rhonda_necklaces = boudreaux_necklaces / half_divisor

    # L2
    three_times_multiplier = 3 # three times as many necklaces
    three_times_rhonda = rhonda_necklaces * three_times_multiplier

    # L3
    four_less = 4 # four less than three times as many necklaces
    latch_necklaces = three_times_rhonda - four_less

    # FA
    answer = latch_necklaces
    return answer