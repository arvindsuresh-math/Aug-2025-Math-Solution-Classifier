def solve():
    """Index: 621.
    Returns: the number of seagulls left.
    """
    # L1
    initial_seagulls = 36 # 36 seagulls on the roof
    scared_away_divisor = 4 # 1/4 of them away
    scared_away_seagulls = initial_seagulls / scared_away_divisor

    # L2
    remaining_after_scared = initial_seagulls - scared_away_seagulls

    # L3
    mcdonalds_divisor = 3 # 1/3 of the remaining birds
    flew_to_mcdonalds = remaining_after_scared / mcdonalds_divisor

    # L4
    final_seagulls = remaining_after_scared - flew_to_mcdonalds

    # FA
    answer = final_seagulls
    return answer