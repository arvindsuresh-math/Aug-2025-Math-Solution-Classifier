def solve():
    """Index: 2950.
    Returns: the total number of open parking spots.
    """
    # L1
    spots_level1 = 4 # 4 open parking spots on the first level
    more_spots_level2 = 7 # 7 more open parking spots on the second level
    spots_level2 = spots_level1 + more_spots_level2

    # L2
    more_spots_level3 = 6 # 6 more open parking spots on the third level
    spots_level3 = spots_level2 + more_spots_level3

    # L3
    spots_level4 = 14 # 14 open parking spots on the fourth level
    total_spots = spots_level1 + spots_level2 + spots_level3 + spots_level4

    # FA
    answer = total_spots
    return answer