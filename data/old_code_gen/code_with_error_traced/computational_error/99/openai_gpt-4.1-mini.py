def solve(
    first_tank_gallons: int = 48,  # There are 48 gallons of water in the first tank
    first_tank_fish_size: int = 3,  # three-inch fish in the first tank
    second_tank_fish_size: int = 2  # two-inch fish in the second tank
):
    """Index: 99.
    Returns: the difference in the number of fish between the first and second tank after one fish in the first tank eats another.
    """

    #: L1
    second_tank_gallons = first_tank_gallons / 2 # eval: 24.0 = 48 / 2

    #: L2
    second_tank_fish_count = second_tank_gallons / second_tank_fish_size # eval: 12.0 = 24.0 / 2

    #: L3
    first_tank_fish_count = first_tank_gallons / first_tank_fish_size # eval: 16.0 = 48 / 3

    #: L4
    first_tank_fish_after_eating = 16.0 # eval: 16.0 = 16.0

    #: L5
    fish_difference = first_tank_fish_after_eating - second_tank_fish_count # eval: 4.0 = 16.0 - 12.0

    #: FA
    answer = fish_difference
    return answer # eval: return 4.0
