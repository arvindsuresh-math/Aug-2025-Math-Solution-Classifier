def solve():
    """Index: 2177.
    Returns: the total number of hours Toby spends pulling the sled.
    """
    # L1
    loaded_speed = 10 # 10 miles per hour if the sled is fully loaded
    loaded_distance_part1 = 180 # pulling the loaded sled for 180 miles
    time_loaded_part1 = loaded_distance_part1 / loaded_speed

    # L2
    unloaded_speed = 20 # 20 miles per hour if the sled is unloaded
    unloaded_distance_part1 = 120 # pulling the unloaded sled for 120 miles
    time_unloaded_part1 = unloaded_distance_part1 / unloaded_speed

    # L3
    loaded_distance_part2 = 80 # pulling the loaded sled 80 miles
    time_loaded_part2 = loaded_distance_part2 / loaded_speed

    # L4
    unloaded_distance_part2 = 140 # pulling the unloaded sled another 140 miles
    time_unloaded_part2 = unloaded_distance_part2 / unloaded_speed

    # L5
    total_time = time_loaded_part1 + time_unloaded_part1 + time_loaded_part2 + time_unloaded_part2

    # FA
    answer = total_time
    return answer