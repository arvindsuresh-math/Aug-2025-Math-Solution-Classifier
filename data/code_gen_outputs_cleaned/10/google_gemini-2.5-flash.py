def solve(
        interval_years: int = 100, # once every hundred years
        total_period_years: int = 300, # Over three hundred years
        total_people_consumed: int = 847, # consumed 847 people
        growth_factor: int = 2 # twice as many people as the last ship
    ):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """
    #: L1
    # Let S be the number of people on the first hundred years’ ship.
    # We will solve for S later.

    #: L2
    # The second hundred years’ ship had twice as many as the first, so it had 2S people.
    # This implies a coefficient for S.

    #: L3
    # The third hundred years’ ship had twice as many as the second, so it had 2 * 2S = 4S people.
    coefficient_first_ship = 1
    coefficient_second_ship = growth_factor
    coefficient_third_ship = growth_factor * growth_factor

    #: L4
    # All the ships had S + 2S + 4S = 7S = 847 people.
    total_coefficient_s = coefficient_first_ship + coefficient_second_ship + coefficient_third_ship

    #: L5
    # Thus, the ship that the monster ate in the first hundred years had S = 847 / 7 = 121 people on it.
    people_on_first_ship = total_people_consumed / total_coefficient_s

    answer = people_on_first_ship # FINAL ANSWER
    return answer