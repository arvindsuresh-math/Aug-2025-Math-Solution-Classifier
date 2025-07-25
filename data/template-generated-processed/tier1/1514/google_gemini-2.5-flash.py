def solve():
    """Index: 1514.
    Returns: the total time Carla spends on activities.
    """
    # L1
    sharpening_time = 10 # 10 minutes sharpening her knife
    peeling_multiplier = 3 # 3 times that amount of time peeling vegetables
    peeling_time = sharpening_time * peeling_multiplier

    # L2
    total_time = peeling_time + sharpening_time

    # FA
    answer = total_time
    return answer