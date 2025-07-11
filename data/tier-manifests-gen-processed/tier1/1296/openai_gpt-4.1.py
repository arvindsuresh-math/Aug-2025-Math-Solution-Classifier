def solve():
    """Index: 1296.
    Returns: the total number of carpets in all 4 houses.
    """
    # L1
    house3_carpets = 10 # 10 carpets in house 3
    house4_multiplier = 2 # house 4 has twice as many carpets as house 3
    house4_carpets = house4_multiplier * house3_carpets

    # L2
    house1_carpets = 12 # 12 carpets in house 1
    house2_carpets = 20 # 20 carpets in house 2
    total_carpets = house1_carpets + house2_carpets + house3_carpets + house4_carpets

    # FA
    answer = total_carpets
    return answer