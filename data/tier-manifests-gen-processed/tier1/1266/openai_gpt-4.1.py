def solve():
    """Index: 1266.
    Returns: the total number of dolls Aida, Sophie, and Vera have combined.
    """
    # L1
    vera_dolls = 20 # Vera has 20 dolls
    sophie_multiplier = 2 # Sophie has twice as many dolls as Vera
    sophie_dolls = sophie_multiplier * vera_dolls

    # L2
    aida_multiplier = 2 # Aida has twice as many dolls as Sophie
    aida_dolls = aida_multiplier * sophie_dolls

    # L3
    total_dolls = aida_dolls + sophie_dolls + vera_dolls

    # FA
    answer = total_dolls
    return answer