def solve():
    """Index: 4808.
    Returns: the total ounces of water Kim drank.
    """
    # L1
    bottle_volume_quarts = 1.5 # 1.5-quart bottle
    ounces_per_quart = 32 # WK
    bottle_volume_ounces = bottle_volume_quarts * ounces_per_quart

    # L2
    can_volume_ounces = 12 # 12 ounce can
    total_ounces_drank = bottle_volume_ounces + can_volume_ounces

    # FA
    answer = total_ounces_drank
    return answer