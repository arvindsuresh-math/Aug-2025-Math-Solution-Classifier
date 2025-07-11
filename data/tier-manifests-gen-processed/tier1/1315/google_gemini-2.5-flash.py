def solve():
    """Index: 1315.
    Returns: the number of pies left.
    """
    # L1
    pies_per_batch = 5 # 5 pies in his oven at once
    num_batches = 7 # bakes 7 batches of pies
    total_pies_baked = pies_per_batch * num_batches

    # L2
    pies_dropped = 8 # drops 8 of them
    pies_left = total_pies_baked - pies_dropped

    # FA
    answer = pies_left
    return answer