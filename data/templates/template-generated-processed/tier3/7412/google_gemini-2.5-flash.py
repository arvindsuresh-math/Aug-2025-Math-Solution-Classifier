def solve():
    """Index: 7412.
    Returns: the total number of pebbles Marcus has now.
    """
    # L1
    initial_pebbles = 18 # Marcus had 18 pebbles
    skipped_divisor = 2 # skipped half of them
    pebbles_left_after_skipping = initial_pebbles / skipped_divisor

    # L2
    pebbles_from_freddy = 30 # Freddy gave him another 30 pebbles
    total_pebbles = pebbles_left_after_skipping + pebbles_from_freddy

    # FA
    answer = total_pebbles
    return answer