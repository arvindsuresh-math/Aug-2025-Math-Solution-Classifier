def solve():
    """Index: 1347.
    Returns: the total number of cabinets Jeff has.
    """
    # L1
    base_cabinets_per_counter_initial = 3 # He currently has 3 cabinets over one counter
    multiplier_twice = 2 # installs twice as many cabinets
    cabinets_per_new_counter = base_cabinets_per_counter_initial * multiplier_twice

    # L2
    num_different_counters = 3 # over 3 different counters each
    total_cabinets_over_new_counters = cabinets_per_new_counter * num_different_counters

    # L3
    additional_cabinets_installed = 5 # installs 5 more cabinets
    total_cabinets_installed_this_time = total_cabinets_over_new_counters + additional_cabinets_installed

    # L4
    final_total_cabinets = total_cabinets_installed_this_time + base_cabinets_per_counter_initial

    # FA
    answer = final_total_cabinets
    return answer