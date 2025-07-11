def solve(
    total_people: int = 847,  # it has consumed 847 people over three hundred years
):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """

    #: L4
    total_ships_factor = 7

    #: L5
    first_ship_people = total_people / total_ships_factor

    #: FA
    answer = first_ship_people
    return answer