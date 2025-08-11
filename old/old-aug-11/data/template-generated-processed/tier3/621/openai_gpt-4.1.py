def solve():
    """Index: 621.
    Returns: the number of seagulls left after the kids scare some away and others fly to McDonald's.
    """
    # L1
    initial_seagulls = 36 # There are 36 seagulls on the roof
    scared_denominator = 4 # Kids scare 1/4 of them away
    scared_away = initial_seagulls / scared_denominator

    # L2
    remaining_after_kids = initial_seagulls - scared_away

    # L3
    mcdonalds_denominator = 3 # 1/3 of the remaining birds decide to fly to McDonald's
    fly_to_mcdonalds = remaining_after_kids / mcdonalds_denominator

    # L4
    seagulls_left = remaining_after_kids - fly_to_mcdonalds

    # FA
    answer = seagulls_left
    return answer