def solve(
    total_people_consumed: int = 847,  # Over three hundred years, it has consumed 847 people
    num_periods: int = 3  # Monster rises once every hundred years over three hundred years
):
    """Index: 10.
    Returns: the number of people on the first ship the monster consumed."""

    #: L4
    total_ship_multiplier = 1 - 2 + 4

    #: L5
    people_on_first_ship = total_people_consumed / total_ship_multiplier

    #: FA
    answer = people_on_first_ship
    return answer