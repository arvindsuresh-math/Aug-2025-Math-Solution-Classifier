def solve():
    """Index: 4541.
    Returns: the total time in minutes to finish making the bread.
    """
    # L1
    rise_time_per_instance = 120 # 120 minutes
    num_rise_instances = 2 # twice
    total_rise_time = rise_time_per_instance * num_rise_instances

    # L2
    kneading_time = 10 # 10 minutes kneading it
    baking_time = 30 # 30 minutes baking it
    total_time = total_rise_time + kneading_time + baking_time

    # FA
    answer = total_time
    return answer