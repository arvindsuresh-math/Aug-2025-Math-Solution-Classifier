def solve(
    every_hundred_years: int = 100, # rises from the waters once every hundred years
    over_three_hundred_years: int = 300, # Over three hundred years
    total_people_consumed: int = 847, # it has consumed 847 people
    twice_as_many: int = 2 # each new ship has twice as many people as the last ship
):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """
    # L1: Let S be the number of people on the first hundred years’ ship. (Implicitly defined as the variable we solve for)
    #: L2
    # The second hundred years’ ship had twice as many as the first, so it had 2S people.
    # This is represented by the factor 'twice_as_many'
    #: L3
    # The third hundred years’ ship had twice as many as the second, so it had 2 * 2S = 4S people.
    multiplier_third_ship = twice_as_many * twice_as_many

    #: L4
    # All the ships had S + 2S + 4S = 7S = 847 people.
    # The total factor is 1 (for the first ship) + 2 (for the second) + 4 (for the third)
    total_factor = 1 + twice_as_many + multiplier_third_ship

    #: L5
    # Thus, the ship that the monster ate in the first hundred years had S = 847 / 7 = 121 people on it.
    people_first_ship = total_people_consumed / total_factor

    answer = people_first_ship # FINAL ANSWER
    return answer