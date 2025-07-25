def solve():
    """Index: 603.
    Returns: the number of empty cans Alyssa and Abigail still need to collect.
    """
    # L1
    alyssa_collected = 30 # Alyssa collected 30
    abigail_collected = 43 # Abigail collected 43 empty cans
    total_collected = alyssa_collected + abigail_collected

    # L2
    required_total = 100 # need to collect 100 empty cans
    still_needed = required_total - total_collected

    # FA
    answer = still_needed
    return answer