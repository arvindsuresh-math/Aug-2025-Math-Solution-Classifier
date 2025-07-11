def solve():
    """Index: 1347.
    Returns: the total number of cabinets Jeff has after all installations.
    """
    # L1
    initial_cabinets_per_counter = 3 # 3 cabinets over one counter
    multiplier = 2 # twice as many cabinets
    cabinets_per_counter = initial_cabinets_per_counter * multiplier

    # L2
    num_counters = 3 # over 3 different counters each
    total_new_cabinets = cabinets_per_counter * num_counters

    # L3
    additional_cabinets = 5 # installs 5 more cabinets
    total_installed = total_new_cabinets + additional_cabinets

    # L4
    total_cabinets = total_installed + initial_cabinets_per_counter

    # FA
    answer = total_cabinets
    return answer