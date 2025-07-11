def solve():
    """Index: 99.
    Returns: the number of more fish Gail would have in the first tank than the second tank.
    """
    # L1
    first_tank_gallons = 48 # 48 gallons of water in the first tank
    size_ratio = 2 # The first tank is twice the size of the second tank
    second_tank_gallons = first_tank_gallons / size_ratio

    # L2
    fish_size_second_tank = 2 # two-inch fish in the second tank
    fish_in_second_tank = second_tank_gallons / fish_size_second_tank

    # L3
    fish_size_first_tank = 3 # three-inch fish in the first tank
    initial_fish_in_first_tank = first_tank_gallons / fish_size_first_tank

    # L4
    eaten_fish = 1 # one of the first tank fish eats another
    fish_in_first_tank_after_eating = initial_fish_in_first_tank - eaten_fish

    # L5
    more_fish_in_first_tank = fish_in_first_tank_after_eating - fish_in_second_tank

    # FA
    answer = more_fish_in_first_tank
    return answer