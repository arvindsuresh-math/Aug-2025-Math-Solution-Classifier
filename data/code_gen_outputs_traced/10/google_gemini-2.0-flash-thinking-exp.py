def solve(
    every_hundred_years: int = 100, # rises from the waters once every hundred years
    over_three_hundred_years: int = 300, # Over three hundred years
    total_people_consumed: int = 847, # it has consumed 847 people
    twice_as_many: int = 2 # each new ship has twice as many people as the last ship
):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """

    #: L3
    multiplier_third_ship = twice_as_many * twice_as_many # eval: 4 = 2 * 2

    #: L4
    total_factor = 1 + twice_as_many + multiplier_third_ship # eval: 7 = 1 + 2 + 4

    #: L5
    people_first_ship = total_people_consumed / total_factor # eval: 121.0 = 847 / 7

    #: FA
    answer = people_first_ship # eval: 121.0 = 121.0
    return answer # eval: return 121.0
