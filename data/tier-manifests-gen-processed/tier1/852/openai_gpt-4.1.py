def solve():
    """Index: 852.
    Returns: the number of ants in the jar after 5 hours.
    """
    # L1
    initial_ants = 50 # 50 ants
    doubling_factor = 2 # number of ants doubles each hour
    after_1hr = initial_ants * doubling_factor

    # L2
    after_2hr = after_1hr * doubling_factor

    # L3
    after_3hr = after_2hr * doubling_factor

    # L4
    after_4hr = after_3hr * doubling_factor

    # L5
    after_5hr = after_4hr * doubling_factor

    # FA
    answer = after_5hr
    return answer