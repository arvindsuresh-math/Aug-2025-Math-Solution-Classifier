def solve():
    """Index: 1501.
    Returns: the weight left on the truck after the two deliveries, in pounds.
    """
    # L1
    initial_load = 50000 # a load of 50000 pounds
    first_store_percent = 0.10 # 10% of the weight gets unloaded at the first store
    first_store_unload = initial_load * first_store_percent

    # L2
    after_first_store = initial_load - first_store_unload

    # L3
    second_store_percent = 0.20 # 20% of the remaining load is removed at the second store
    second_store_unload = after_first_store * second_store_percent

    # L4
    after_second_store = after_first_store - second_store_unload

    # FA
    answer = after_second_store
    return answer