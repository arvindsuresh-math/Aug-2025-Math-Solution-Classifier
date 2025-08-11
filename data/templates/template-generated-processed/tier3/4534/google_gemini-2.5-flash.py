def solve():
    """Index: 4534.
    Returns: the number of Easter eggs Hannah found.
    """
    # L1
    hannah_ratio_multiplier = 2 # twice as many as Helen
    helen_ratio_unit = 1 # implied from "twice as many as Helen"
    total_units = hannah_ratio_multiplier + helen_ratio_unit

    # L2
    total_easter_eggs = 63 # 63 Easter eggs
    eggs_per_unit = total_easter_eggs / total_units

    # L3
    hannah_found = hannah_ratio_multiplier * eggs_per_unit

    # FA
    answer = hannah_found
    return answer