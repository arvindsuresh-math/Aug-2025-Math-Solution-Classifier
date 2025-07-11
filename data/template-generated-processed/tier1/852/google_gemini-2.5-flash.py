def solve():
    """Index: 852.
    Returns: the number of ants in the jar after 5 hours.
    """
    # L1
    initial_ants = 50 # 50 ants
    doubling_factor = 2 # doubles each hour
    ants_after_1_hour = initial_ants * doubling_factor

    # L2
    ants_after_2_hours = ants_after_1_hour * doubling_factor

    # L3
    ants_after_3_hours = ants_after_2_hours * doubling_factor

    # L4
    ants_after_4_hours = ants_after_3_hours * doubling_factor

    # L5
    ants_after_5_hours = ants_after_4_hours * doubling_factor

    # FA
    answer = ants_after_5_hours
    return answer