def solve(
        first_tank_water_gallons: int = 48, # 48 gallons of water in the first tank
        first_tank_size_multiplier: int = 2, # The first tank is twice the size of the second tank
        gallons_per_inch_fish: int = 1, # one gallon of water per inch of fish (this argument is not directly used in calculations but represents the rule)
        second_tank_fish_size: int = 2, # two-inch fish in the second tank
        first_tank_fish_size: int = 3, # three-inch fish in the first tank
        fish_eaten_in_first_tank: int = 1 # one of the first tank fish eats another
    ):
    """Index: 99.
    Returns: the number of more fish in the first tank than the second tank after one fish is eaten.
    """

    #: L1
    second_tank_gallons = first_tank_water_gallons / first_tank_size_multiplier # eval: 24.0 = 48 / 2

    #: L2
    fish_in_second_tank = second_tank_gallons / second_tank_fish_size # eval: 12.0 = 24.0 / 2

    #: L3
    initial_fish_in_first_tank = first_tank_water_gallons / first_tank_fish_size # eval: 16.0 = 48 / 3

    #: L4
    final_fish_in_first_tank = initial_fish_in_first_tank - fish_eaten_in_first_tank # eval: 15.0 = 16.0 - 1

    #: L5
    more_fish_in_first_tank = final_fish_in_first_tank - fish_in_second_tank # eval: 3.0 = 15.0 - 12.0

    #: FA
    answer = more_fish_in_first_tank
    return answer # eval: return 3.0
