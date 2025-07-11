def solve():
    """Index: 1954.
    Returns: the total number of foreign objects caught in the dog's fur.
    """
    # L1
    num_burrs = 12 # Andrew's dog has 12 burrs
    ticks_per_burr_multiplier = 6 # six times as many ticks as burrs
    num_ticks = num_burrs * ticks_per_burr_multiplier

    # L2
    total_foreign_objects = num_ticks + num_burrs

    # FA
    answer = total_foreign_objects
    return answer