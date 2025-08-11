def solve():
    """Index: 1494.
    Returns: the total number of fish the boys have in total.
    """
    # L1
    micah_fish = 7 # Micah has 7 fish in his aquarium
    kenneth_multiplier = 3 # Kenneth has three times as many fish
    kenneth_fish = micah_fish * kenneth_multiplier

    # L2
    matthias_less_than_kenneth = 15 # Matthias has 15 less fish than Kenneth
    matthias_fish = kenneth_fish - matthias_less_than_kenneth

    # L3
    total_fish = micah_fish + kenneth_fish + matthias_fish

    # FA
    answer = total_fish
    return answer