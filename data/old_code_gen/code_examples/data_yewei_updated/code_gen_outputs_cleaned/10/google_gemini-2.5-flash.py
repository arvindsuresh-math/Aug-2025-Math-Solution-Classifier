def solve(
        frequency_years: int = 100,  # once every hundred years
        total_period_years: int = 300,  # Over three hundred years
        total_people_consumed: int = 847,  # consumed 847 people
        growth_factor: int = 2  # each new ship has twice as many people as the last ship
    ):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """
    #: L1
    # Let first_ship_people be the number of people on the first ship (S)

    #: L2
    # The second ship had twice as many people as the first, so it had 2S people.
    # This means its factor relative to the first ship is 'growth_factor'.
    second_ship_factor = growth_factor

    #: L3
    # The third ship had twice as many as the second, so it had 2 * 2S = 4S people.
    third_ship_factor = growth_factor * second_ship_factor

    #: L4
    # All the ships had S + 2S + 4S = 7S = 847 people.
    total_factor_sum = 1 + second_ship_factor + third_ship_factor

    #: L5
    # Thus, the ship that the monster ate in the first hundred years had S = 847 / 7 = 121 people on it.
    first_ship_people = total_people_consumed / total_factor_sum

    answer = first_ship_people # FINAL ANSWER
    return answer