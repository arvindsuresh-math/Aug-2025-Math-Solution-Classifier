def solve():
    """Index: 3269.
    Returns: the total liters of water in 2 buckets.
    """
    # L1
    jugs_per_bucket = 4 # 4 jugs
    jug_capacity_liters = 5 # 5 liters of water
    liters_per_bucket = jugs_per_bucket * jug_capacity_liters

    # L2
    num_buckets = 2 # 2 buckets
    total_liters = liters_per_bucket * num_buckets

    # FA
    answer = total_liters
    return answer