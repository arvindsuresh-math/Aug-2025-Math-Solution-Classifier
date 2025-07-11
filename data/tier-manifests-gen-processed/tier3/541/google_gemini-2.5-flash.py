def solve():
    """Index: 541.
    Returns: the number of lego sets Tonya buys.
    """
    # L1
    num_dolls = 4 # 4 dolls
    cost_per_doll = 15 # $15 each
    spent_on_younger_sister = num_dolls * cost_per_doll

    # L2
    cost_per_lego_set = 20 # They cost $20 each
    num_lego_sets = spent_on_younger_sister / cost_per_lego_set

    # FA
    answer = num_lego_sets
    return answer