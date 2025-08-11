def solve():
    """Index: 6374.
    Returns: the number of double-flips Tyler did.
    """
    # L1
    jen_triple_flips = 16 # sixteen triple-flips
    flips_per_triple_flip = 3 # triple-flip
    jen_total_flips = jen_triple_flips * flips_per_triple_flip

    # L2
    half_divisor = 2 # half the number of times
    tyler_total_flips = jen_total_flips / half_divisor

    # L3
    flips_per_double_flip = 2 # double-flip
    tyler_double_flips = tyler_total_flips / flips_per_double_flip

    # FA
    answer = tyler_double_flips
    return answer