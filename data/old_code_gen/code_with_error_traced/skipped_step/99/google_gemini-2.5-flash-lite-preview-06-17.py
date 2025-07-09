def solve(
    gallons_in_first_tank: int = 48, # There are 48 gallons of water in the first tank.
    ratio_first_to_second_tank: int = 2, # The first tank is twice the size of the second tank.
    fish_size_second_tank: int = 2, # she keeps two-inch fish in the second tank
    fish_size_first_tank: int = 3, # and three-inch fish in the first tank
    fish_eaten_in_first_tank: int = 1 # one of the first tank fish eats another
):
    """Index: 99.
    Returns: how many more fish would Gail have in the first tank than the second tank.
    """

    #: L1
    gallons_in_second_tank = gallons_in_first_tank / ratio_first_to_second_tank # eval: 24.0 = 48 / 2

    #: L2
    num_fish_second_tank = gallons_in_second_tank / fish_size_second_tank # eval: 12.0 = 24.0 / 2

    #: L3

    #: L4
    num_fish_first_tank_after_eating = ratio_first_to_second_tank - fish_eaten_in_first_tank # eval: 1 = 2 - 1

    #: L5
    difference_in_fish = num_fish_first_tank_after_eating - num_fish_second_tank # eval: -11.0 = 1 - 12.0

    #: FA
    answer = difference_in_fish
    return answer # eval: return -11.0
