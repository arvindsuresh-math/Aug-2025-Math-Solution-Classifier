def solve():
    """Index: 1060.
    Returns: the total number of earrings Alissa has now.
    """
    # L1
    pairs_bought = 12 # 12 pairs of earrings
    earrings_per_pair = 2 # 1 pair of earrings equals 2 earrings
    total_earrings_barbie_bought = pairs_bought * earrings_per_pair

    # L2
    half_divisor = 2 # gave half of them to Alissa
    earrings_given_to_alissa = total_earrings_barbie_bought / half_divisor

    # L3
    triple_factor = 3 # triple the number of earrings she was given
    alissa_total_earrings = earrings_given_to_alissa * triple_factor

    # FA
    answer = alissa_total_earrings
    return answer