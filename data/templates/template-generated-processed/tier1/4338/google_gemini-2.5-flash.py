def solve():
    """Index: 4338.
    Returns: the total number of fish in the tank.
    """
    # L1
    spotted_blue_fish = 10 # 10 blue, spotted fish
    multiplier_for_blue_fish = 2 # half of the blue fish have spots
    blue_fish = multiplier_for_blue_fish * spotted_blue_fish

    # L2
    multiplier_for_total_fish = 3 # One third of them are blue
    total_fish = multiplier_for_total_fish * blue_fish

    # FA
    answer = total_fish
    return answer