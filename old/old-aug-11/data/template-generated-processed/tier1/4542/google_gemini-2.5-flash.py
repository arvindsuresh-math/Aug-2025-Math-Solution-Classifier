def solve():
    """Index: 4542.
    Returns: the total number of fish.
    """
    # L1
    fish_in_first_tank = 20 # 1 of the tanks has 20 fish in it
    multiplier_for_other_tanks = 2 # twice as many fish
    fish_in_other_tanks = fish_in_first_tank * multiplier_for_other_tanks

    # L2
    num_other_tanks = 2 # the other two have twice as many fish
    total_fish = fish_in_first_tank + fish_in_other_tanks * num_other_tanks

    # FA
    answer = total_fish
    return answer