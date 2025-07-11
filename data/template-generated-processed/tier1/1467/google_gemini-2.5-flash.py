def solve():
    """Index: 1467.
    Returns: the number of bottle caps Sammy has.
    """
    # L1
    billie_caps = 2 # If Billie has 2 bottle caps
    janine_multiplier = 3 # Janine has 3 times as many bottle caps as Billie
    janine_caps = billie_caps * janine_multiplier

    # L2
    sammy_more_than_janine = 2 # Sammy has 2 more bottle caps than Janine
    sammy_caps = janine_caps + sammy_more_than_janine

    # FA
    answer = sammy_caps
    return answer