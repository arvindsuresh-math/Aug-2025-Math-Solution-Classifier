def solve(
    total_people_consumed: int = 847,  # Over three hundred years, it has consumed 847 people
    num_periods: int = 3  # Monster rises once every hundred years over three hundred years
):
    """Index: 10.
    Returns: the number of people on the first ship the monster consumed."""

    #: L4
    total_ship_multiplier = 17 # eval: 17 = 17

    #: L5
    people_on_first_ship = total_people_consumed / total_ship_multiplier # eval: 49.8235294117647 = 847 / 17

    #: FA
    answer = people_on_first_ship
    return answer # eval: return 49.8235294117647
