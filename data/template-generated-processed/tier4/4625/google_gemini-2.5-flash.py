def solve():
    """Index: 4625.
    Returns: the number of baby carrots left over.
    """
    # L1
    total_carrots = 47 # 47 baby carrots
    num_goats = 4 # four goats
    carrots_per_goat_raw = total_carrots / num_goats

    # L2
    carrots_per_goat_even = int(carrots_per_goat_raw)

    # L3
    total_carrots_fed = carrots_per_goat_even * num_goats

    # L4
    carrots_left_over = total_carrots - total_carrots_fed

    # FA
    answer = carrots_left_over
    return answer