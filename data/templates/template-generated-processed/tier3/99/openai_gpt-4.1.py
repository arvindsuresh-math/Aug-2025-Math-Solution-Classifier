def solve():
    """Index: 99.
    Returns: the number of more fish Gail would have in the first tank than the second tank after one fish eats another.
    """
    # L1
    first_tank_gallons = 48 # 48 gallons of water in the first tank
    tank_size_ratio = 2 # first tank is twice the size of the second tank
    second_tank_gallons = first_tank_gallons / tank_size_ratio

    # L2
    second_tank_fish_size = 2 # two-inch fish in the second tank
    second_tank_fish = second_tank_gallons / second_tank_fish_size

    # L3
    first_tank_fish_size = 3 # three-inch fish in the first tank
    first_tank_fish = first_tank_gallons / first_tank_fish_size

    # L4
    eaten_fish = 1 # one of the first tank fish eats another
    first_tank_fish_after_eating = first_tank_fish - eaten_fish

    # L5
    fish_difference = first_tank_fish_after_eating - second_tank_fish

    # FA
    answer = fish_difference
    return answer