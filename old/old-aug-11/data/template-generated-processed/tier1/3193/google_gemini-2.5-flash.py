def solve():
    """Index: 3193.
    Returns: the total time to make smoothies.
    """
    # L1
    num_smoothies = 5 # 5 smoothies
    minutes_per_smoothie = 3 # 3 minutes per smoothie
    time_making_smoothies = num_smoothies * minutes_per_smoothie

    # L2
    time_to_freeze_ice_cubes = 40 # 40 minutes to freeze ice cubes
    total_time = time_making_smoothies + time_to_freeze_ice_cubes

    # FA
    answer = total_time
    return answer