def solve():
    """Index: 839.
    Returns: the total number of eggs needed to buy.
    """
    # L1
    small_child_omelet_portion = 0.5 # small children can eat a half omelet
    small_children_tickets = 53 # 53 small children tickets
    omelets_small_children = small_child_omelet_portion * small_children_tickets

    # L2
    older_child_omelet_portion = 1 # older children can eat a whole omelet
    older_children_tickets = 35 # 35 older children tickets
    omelets_older_children = older_child_omelet_portion * older_children_tickets

    # L3
    adult_omelet_portion = 2 # adults will eat two omelets
    adult_tickets = 75 # 75 adult tickets
    omelets_adults = adult_omelet_portion * adult_tickets

    # L4
    senior_omelet_portion = 1.5 # seniors will eat one and a half omelets
    senior_tickets = 37 # 37 senior tickets
    omelets_seniors = senior_omelet_portion * senior_tickets

    # L5
    extra_omelets = 25 # 25 extra omelets
    total_omelets_needed = omelets_small_children + omelets_older_children + omelets_adults + omelets_seniors + extra_omelets

    # L6
    eggs_per_omelet = 2 # 2 eggs for each omelet
    total_eggs_needed = eggs_per_omelet * total_omelets_needed

    # FA
    answer = total_eggs_needed
    return answer