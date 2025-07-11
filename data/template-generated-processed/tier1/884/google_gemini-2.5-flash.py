def solve():
    """Index: 884.
    Returns: the total number of vampires after two nights.
    """
    # L1
    people_turned_per_vampire_per_night = 5 # each vampire turns 5 more people
    initial_vampires = 2 # Two vampires have come
    new_vampires_night1 = people_turned_per_vampire_per_night * initial_vampires

    # L2
    total_vampires_after_night1 = new_vampires_night1 + initial_vampires

    # L3
    new_vampires_night2 = people_turned_per_vampire_per_night * total_vampires_after_night1

    # L4
    total_vampires_after_night2 = new_vampires_night2 + total_vampires_after_night1

    # FA
    answer = total_vampires_after_night2
    return answer