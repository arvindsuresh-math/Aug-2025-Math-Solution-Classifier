def solve(
    total_people_eaten: int = 847, # Over three hundred years, it has consumed 847 people.
    years_between_feasts: int = 100, # once every hundred years
    total_years: int = 300 # Over three hundred years
):
    """Index: 10.
    Returns: the number of people on the ship the monster ate in the first hundred years.
    """

    #: L4
    total_proportions = 1 + 2 + 4

    #: L5
    people_on_first_ship = total_people_eaten / total_proportions

    answer = people_on_first_ship # FINAL ANSWER
    return answer