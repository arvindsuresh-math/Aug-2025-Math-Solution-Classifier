def solve():
    """Index: 2441.
    Returns: the number of blue, spotted fish.
    """
    # L1
    total_fish = 30 # 30 fish in the tank
    blue_fraction_denominator = 3 # One third of them are blue
    blue_fish = total_fish / blue_fraction_denominator

    # L2
    spotted_fraction_denominator = 2 # half of the blue fish have spots
    blue_spotted_fish = blue_fish / spotted_fraction_denominator

    # FA
    answer = blue_spotted_fish
    return answer