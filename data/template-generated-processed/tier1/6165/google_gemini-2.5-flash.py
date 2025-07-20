def solve():
    """Index: 6165.
    Returns: the number of orange shells.
    """
    # L1
    purple_shells = 13 # 13 purple shells
    pink_shells = 8 # 8 pink shells
    yellow_shells = 18 # 18 yellow shells
    blue_shells = 12 # 12 blue shells
    non_orange_shells = purple_shells + pink_shells + yellow_shells + blue_shells

    # L2
    total_shells = 65 # 65 shells in total
    orange_shells = total_shells - non_orange_shells

    # FA
    answer = orange_shells
    return answer