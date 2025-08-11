def solve():
    """Index: 357.
    Returns: the total number of fish Catriona has in her aquarium.
    """
    # L1
    goldfish = 8 # 8 goldfish in her aquarium
    angelfish_more_than_goldfish = 4 # 4 more angelfish than goldfish
    angelfish = goldfish + angelfish_more_than_goldfish

    # L2
    guppies_multiplier = 2 # twice as many guppies as angelfish
    guppies = angelfish * guppies_multiplier

    # L3
    total_fish = goldfish + angelfish + guppies

    # FA
    answer = total_fish
    return answer