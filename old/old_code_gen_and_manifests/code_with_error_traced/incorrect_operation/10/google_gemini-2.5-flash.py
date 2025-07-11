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
    coefficient_third_ship = growth_factor - growth_factor # eval: 0 = 2 - 2

    #: L4
    total_coefficient_s = coefficient_first_ship + coefficient_second_ship + coefficient_third_ship # eval: 3 = 1 + 2 + 0

    #: L5
    people_on_first_ship = total_people_consumed / total_coefficient_s # eval: 282.3333333333333 = 847 / 3

    #: FA
    answer = people_on_first_ship
    return answer # eval: return 282.3333333333333
