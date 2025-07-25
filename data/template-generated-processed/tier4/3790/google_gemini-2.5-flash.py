def solve():
    """Index: 3790.
    Returns: the number of jars James needs to buy.
    """
    # L1
    num_hives = 5 # 5 hives
    liters_per_hive = 20 # each produce 20 liters of honey
    total_honey_produced = num_hives * liters_per_hive

    # L2
    honey_kept_divisor = 2 # half the honey
    honey_james_keeps = total_honey_produced / honey_kept_divisor

    # L3
    jar_capacity = 0.5 # Each jar can hold .5 liters
    jars_needed = honey_james_keeps / jar_capacity

    # FA
    answer = jars_needed
    return answer