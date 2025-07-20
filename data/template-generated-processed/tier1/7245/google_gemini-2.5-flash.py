def solve():
    """Index: 7245.
    Returns: the total number of napkins William has now.
    """
    # L1
    william_initial_napkins = 15 # William had 15 napkins before
    olivia_gave_napkins = 10 # Olivia gave William 10 napkins
    william_after_olivia = william_initial_napkins + olivia_gave_napkins

    # L2
    multiplier_twice = 2 # twice the number of napkins
    amelia_gave_napkins = multiplier_twice * olivia_gave_napkins

    # L3
    total_napkins = amelia_gave_napkins + william_after_olivia

    # FA
    answer = total_napkins
    return answer