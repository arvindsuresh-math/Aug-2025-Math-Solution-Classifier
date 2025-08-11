def solve():
    """Index: 1882.
    Returns: the initial number of bananas on the tree.
    """
    # L1
    raj_eaten = 70 # Raj has eaten 70 bananas
    raj_remaining_multiplier = 2 # has twice as many remaining
    raj_remaining = raj_remaining_multiplier * raj_eaten

    # L2
    total_cut = raj_remaining + raj_eaten

    # L3
    bananas_left = 100 # 100 bananas left after Raj cut some bananas
    initial_bananas = bananas_left + total_cut

    # FA
    answer = initial_bananas
    return answer