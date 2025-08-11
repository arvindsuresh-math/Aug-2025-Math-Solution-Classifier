def solve():
    """Index: 5978.
    Returns: the number of bracelets Caitlin can make.
    """
    # L1
    total_beads = 528 # Caitlin has 528 beads
    equal_parts = 2 # equal amounts of large and small beads
    total_small_beads = total_beads / equal_parts

    # L2
    large_beads_per_bracelet = 12 # each bracelet uses 12 large beads
    small_beads_multiplier = 2 # twice as many small beads
    small_beads_per_bracelet = large_beads_per_bracelet * small_beads_multiplier

    # L3
    num_bracelets = total_small_beads / small_beads_per_bracelet

    # FA
    answer = num_bracelets
    return answer