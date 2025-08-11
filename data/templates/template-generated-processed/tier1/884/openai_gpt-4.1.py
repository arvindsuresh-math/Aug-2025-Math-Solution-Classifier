def solve():
    """Index: 884.
    Returns: the number of vampires after two nights.
    """
    # L1
    people_turned_per_vampire = 5 # each vampire turns 5 more people into vampires
    starting_vampires = 2 # two vampires
    new_vampires_night1 = people_turned_per_vampire * starting_vampires

    # L2
    total_vampires_night1 = new_vampires_night1 + starting_vampires

    # L3
    new_vampires_night2 = people_turned_per_vampire * total_vampires_night1

    # L4
    total_vampires_night2 = new_vampires_night2 + total_vampires_night1

    # FA
    answer = total_vampires_night2
    return answer