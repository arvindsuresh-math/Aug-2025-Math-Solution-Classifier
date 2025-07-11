def solve():
    """Index: 231.
    Returns: the number of beakers without copper ions that were tested.
    """
    # L1
    total_drops_used = 45 # 45 drops are used before all 8 beakers with copper ions are found
    drops_per_beaker = 3 # Adding three drops of a solution will turn the liquid in a beaker blue
    beakers_tested = total_drops_used / drops_per_beaker

    # L2
    beakers_with_copper = 8 # 8 of the beakers have copper ions in them
    beakers_without_copper_tested = beakers_tested - beakers_with_copper

    # FA
    answer = beakers_without_copper_tested
    return answer