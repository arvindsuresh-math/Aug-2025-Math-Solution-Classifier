def solve():
    """Index: 231.
    Returns: the number of beakers without copper ions that were tested.
    """
    # L1
    total_drops_used = 45 # 45 drops are used
    drops_per_beaker_with_copper = 3 # three drops of a solution will turn the liquid in a beaker blue
    total_beakers_tested = total_drops_used / drops_per_beaker_with_copper

    # L2
    beakers_with_copper_ions = 8 # 8 of the beakers have copper ions in them
    beakers_without_copper_tested = total_beakers_tested - beakers_with_copper_ions

    # FA
    answer = beakers_without_copper_tested
    return answer