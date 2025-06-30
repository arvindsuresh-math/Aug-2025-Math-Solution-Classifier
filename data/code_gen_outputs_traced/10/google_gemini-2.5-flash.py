def solve(
        interval_years: int = 100, # once every hundred years
        total_period_years: int = 300, # Over three hundred years
        total_people_consumed: int = 847, # consumed 847 people
        growth_factor: int = 2 # twice as many people as the last ship
    ):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """

    #: L3
    coefficient_first_ship = 1 # eval: 1 = 1
    coefficient_second_ship = growth_factor # eval: 2 = 2
    coefficient_third_ship = growth_factor * growth_factor # eval: 4 = 2 * 2

    #: L4
    total_coefficient_s = coefficient_first_ship + coefficient_second_ship + coefficient_third_ship # eval: 7 = 1 + 2 + 4

    #: L5
    people_on_first_ship = total_people_consumed / total_coefficient_s # eval: 121.0 = 847 / 7

    #: FA
    answer = people_on_first_ship # eval: 121.0 = 121.0
    return answer # eval: return 121.0
