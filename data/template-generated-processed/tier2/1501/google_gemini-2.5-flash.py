def solve():
    """Index: 1501.
    Returns: the weight, in pounds, left on the truck after the two deliveries.
    """
    # L1
    initial_load = 50000 # load of 50000 pounds
    first_store_unload_percent = 0.10 # 10% of the weight
    first_store_unloaded_weight = initial_load * first_store_unload_percent

    # L2
    weight_after_first_store = initial_load - first_store_unloaded_weight

    # L3
    second_store_unload_percent = 0.20 # 20% of the remaining load
    second_store_unloaded_weight = weight_after_first_store * second_store_unload_percent

    # L4
    final_weight_left = weight_after_first_store - second_store_unloaded_weight

    # FA
    answer = final_weight_left
    return answer