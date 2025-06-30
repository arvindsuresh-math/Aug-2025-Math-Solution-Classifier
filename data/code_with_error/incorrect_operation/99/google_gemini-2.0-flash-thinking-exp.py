def solve(
    gallons_tank1: int = 48, # 48 gallons of water in the first tank
    size_factor: int = 2, # The first tank is twice the size of the second tank
    gallons_per_inch: int = 1, # one gallon of water per inch of fish
    fish_length_tank2: int = 2, # two-inch fish in the second tank
    fish_length_tank1: int = 3 # three-inch fish in the first tank
):
    """Index: 99.
    Returns: the difference in the number of fish between the first and second tanks after one fish is eaten in the first tank.
    """

    #: L1
    gallons_tank2 = gallons_tank1 / size_factor

    #: L2
    fish_tank2 = gallons_tank2 / fish_length_tank2

    #: L3
    initial_fish_tank1 = gallons_tank1 / fish_length_tank1

    #: L4
    fish_tank1_after_eating = initial_fish_tank1 + 1

    #: L5
    difference_in_fish = fish_tank1_after_eating - fish_tank2

    #: FA
    answer = difference_in_fish
    return answer