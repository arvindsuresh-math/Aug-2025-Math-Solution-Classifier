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
    multiplier_third_ship = every_hundred_years * twice_as_many # eval: 200 = 100 * 2

    #: L4
    total_factor = 1 + twice_as_many + multiplier_third_ship # eval: 203 = 1 + 2 + 200

    #: L5
    people_first_ship = total_people_consumed / total_factor # eval: 4.172413793103448 = 847 / 203

    #: FA
    answer = people_first_ship
    return answer # eval: return 4.172413793103448
