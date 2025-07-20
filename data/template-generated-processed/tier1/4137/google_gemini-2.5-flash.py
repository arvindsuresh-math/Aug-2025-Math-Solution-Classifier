def solve():
    """Index: 4137.
    Returns: the number of cakes left after some were eaten.
    """
    # L1
    diego_baked = 12 # Diego baked 12 cakes
    donald_baked = 4 # Donald also baked 4 cakes
    total_baked = diego_baked + donald_baked

    # L2
    cake_eaten = 1 # Donald ... ate 1 while waiting for the party to start
    cakes_left = total_baked - cake_eaten

    # FA
    answer = cakes_left
    return answer