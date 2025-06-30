def solve(
    total_people_consumed: int = 847,  # Over three hundred years, it has consumed 847 people
    num_periods: int = 3  # Monster rises once every hundred years over three hundred years
):
    """Index: 10.
    Returns: the number of people on the first ship the monster consumed."""
    #: L4
    total_ship_multiplier = 1 + 2 + 4 # eval: 7 = 1 + 2 + 4
    #: L5
    people_on_first_ship = total_people_consumed / total_ship_multiplier # eval: 121.0 = 847 / 7
    answer = people_on_first_ship  # FINAL ANSWER # eval: 121.0 = 121.0  # FINAL ANSWER
    return answer # eval: return 121.0