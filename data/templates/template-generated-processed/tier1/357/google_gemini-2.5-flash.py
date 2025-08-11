def solve():
    """Index: 357.
    Returns: the total number of fish Catriona has in her aquarium.
    """
    # L1
    goldfish = 8 # 8 goldfish
    more_angelfish = 4 # 4 more angelfish than goldfish
    angelfish = goldfish + more_angelfish

    # L2
    multiplier_guppies = 2 # twice as many guppies
    guppies = angelfish * multiplier_guppies

    # L3
    total_fish = goldfish + angelfish + guppies

    # FA
    answer = total_fish
    return answer