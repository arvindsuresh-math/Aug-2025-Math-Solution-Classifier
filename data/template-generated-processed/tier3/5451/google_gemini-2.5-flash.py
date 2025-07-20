def solve():
    """Index: 5451.
    Returns: the total cost Carolyn spends on lace.
    """
    # L1
    hem_length = 300 # the hem is 300 cm long
    waist_divisor = 3 # the waist is a third of the length of the hem
    waist_length = hem_length / waist_divisor

    # L2
    num_cuffs = 2 # Each cuff
    cuff_length = 50 # Each cuff is 50 cm long
    total_cuff_lace = num_cuffs * cuff_length

    # L3
    num_ruffles = 5 # 5 ruffles
    ruffle_length = 20 # each use 20 cm of lace
    total_ruffle_lace = num_ruffles * ruffle_length

    # L4
    total_lace_cm = total_cuff_lace + waist_length + total_ruffle_lace + hem_length

    # L5
    cm_per_meter = 100 # WK
    total_lace_m = total_lace_cm / cm_per_meter

    # L6
    cost_per_meter = 6 # lace costs $6/m
    total_cost = total_lace_m * cost_per_meter

    # FA
    answer = total_cost
    return answer