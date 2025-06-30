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
    multiplier_third_ship = every_hundred_years * twice_as_many

    #: L4
    total_factor = 1 + twice_as_many + multiplier_third_ship

    #: L5
    people_first_ship = total_people_consumed / total_factor

    #: FA
    answer = people_first_ship
    return answer