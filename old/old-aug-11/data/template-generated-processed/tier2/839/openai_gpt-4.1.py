def solve():
    """Index: 839.
    Returns: the total number of eggs the Rotary Club will need to buy.
    """
    # L1
    small_child_omelet_per = 0.5 # small children can eat a half omelet
    num_small_child = 53 # 53 small children tickets
    small_child_omelets = small_child_omelet_per * num_small_child

    # L2
    older_child_omelet_per = 1 # older children can eat a whole omelet
    num_older_child = 35 # 35 older children tickets
    older_child_omelets = older_child_omelet_per * num_older_child

    # L3
    adult_omelet_per = 2 # adults will eat two omelets
    num_adult = 75 # 75 adult tickets
    adult_omelets = adult_omelet_per * num_adult

    # L4
    senior_omelet_per = 1.5 # seniors will eat one and a half omelets
    num_senior = 37 # 37 senior tickets
    senior_omelets = senior_omelet_per * num_senior

    # L5
    extra_omelets = 25 # 25 extra omelets
    total_omelets = small_child_omelets + older_child_omelets + adult_omelets + senior_omelets + extra_omelets

    # L6
    eggs_per_omelet = 2 # 2 eggs for each omelet
    total_eggs = eggs_per_omelet * total_omelets

    # FA
    answer = total_eggs
    return answer