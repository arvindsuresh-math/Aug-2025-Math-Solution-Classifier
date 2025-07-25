def solve():
    """Index: 1286.
    Returns: the total number of fish in Olga's aquarium.
    """
    # L1
    yellow_fish = 12 # 12 yellow ones
    blue_ratio = 0.5 # half as many blue ones
    blue_fish = yellow_fish * blue_ratio

    # L2
    green_ratio = 2 # twice as many green ones as yellow ones
    green_fish = yellow_fish * green_ratio

    # L3
    total_fish = yellow_fish + blue_fish + green_fish

    # FA
    answer = total_fish
    return answer