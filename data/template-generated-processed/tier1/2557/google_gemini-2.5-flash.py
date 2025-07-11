def solve():
    """Index: 2557.
    Returns: the total number of precious stones they have together.
    """
    # L1
    agate_stones = 30 # agate has 30 precious stones
    olivine_more_than_agate = 5 # Olivine has 5 more precious stones than agate
    olivine_stones = agate_stones + olivine_more_than_agate

    # L2
    olivine_agate_total = olivine_stones + agate_stones

    # L3
    diamond_more_than_olivine = 11 # diamond has 11 more precious stones than olivine
    diamond_stones = olivine_stones + diamond_more_than_olivine

    # L4
    total_stones = olivine_agate_total + diamond_stones

    # FA
    answer = total_stones
    return answer