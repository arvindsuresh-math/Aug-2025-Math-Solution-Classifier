def solve():
    """Index: 1954.
    Returns: the total number of foreign objects caught in the dog's fur.
    """
    # L1
    burrs = 12 # 12 burrs
    ticks_per_burr = 6 # six times as many ticks as burrs
    ticks = burrs * ticks_per_burr

    # L2
    total_objects = ticks + burrs

    # FA
    answer = total_objects
    return answer