def solve():
    """Index: 603.
    Returns: the number of additional empty cans needed.
    """
    # L1
    alyssa_collected = 30 # Alyssa collected 30
    abigail_collected = 43 # Abigail collected 43 empty cans
    total_collected = alyssa_collected + abigail_collected

    # L2
    cans_needed_total = 100 # collect 100 empty cans
    cans_remaining_to_collect = cans_needed_total - total_collected

    # FA
    answer = cans_remaining_to_collect
    return answer