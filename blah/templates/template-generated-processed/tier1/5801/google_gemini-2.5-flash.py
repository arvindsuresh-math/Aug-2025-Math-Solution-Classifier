def solve():
    """Index: 5801.
    Returns: the total number of animals Aubree saw that day.
    """
    # L1
    initial_beavers = 20 # 20 beavers
    initial_chipmunks = 40 # 40 chipmunks
    animals_going_to_school = initial_chipmunks + initial_beavers

    # L2
    doubled_factor = 2 # WK
    beavers_coming_back = initial_beavers * doubled_factor

    # L3
    chipmunks_decrease = 10 # decreased by 10
    chipmunks_coming_back = initial_chipmunks - chipmunks_decrease

    # L4
    total_animals_that_day = chipmunks_coming_back + beavers_coming_back + animals_going_to_school

    # FA
    answer = total_animals_that_day
    return answer