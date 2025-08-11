def solve():
    """Index: 3480.
    Returns: the total time it took Chelsea to make the cupcakes.
    """
    # L1
    num_batches = 4 # 4 batches of cupcakes
    baking_time_per_batch = 20 # 20 minutes to bake
    total_baking_time = num_batches * baking_time_per_batch

    # L2
    icing_time_per_batch = 30 # 30 minutes to ice per batch
    total_icing_time = num_batches * icing_time_per_batch

    # L3
    total_time = total_baking_time + total_icing_time

    # FA
    answer = total_time
    return answer