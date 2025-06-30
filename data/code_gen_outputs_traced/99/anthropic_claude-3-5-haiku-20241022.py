def solve(
    first_tank_water: int = 48,  # There are 48 gallons of water in the first tank
    fish_size_first_tank: int = 3,  # three-inch fish in the first tank
    fish_size_second_tank: int = 2  # two-inch fish in the second tank
):
    """Index: 99.
    Returns: the number of more fish Gail would have in the first tank than the second tank after one fish eats another.
    """
    #: L1
    second_tank_water = first_tank_water / 2 # eval: 24.0 = 48 / 2
    #: L2
    fish_in_second_tank = second_tank_water / fish_size_second_tank # eval: 12.0 = 24.0 / 2
    #: L3
    fish_in_first_tank = first_tank_water / fish_size_first_tank # eval: 16.0 = 48 / 3
    #: L4
    fish_in_first_tank_after_eating = fish_in_first_tank - 1 # eval: 15.0 = 16.0 - 1
    #: L5
    difference_in_fish = fish_in_first_tank_after_eating - fish_in_second_tank # eval: 3.0 = 15.0 - 12.0
    answer = difference_in_fish  # FINAL ANSWER # eval: 3.0 = 3.0  # FINAL ANSWER
    return answer # eval: return 3.0