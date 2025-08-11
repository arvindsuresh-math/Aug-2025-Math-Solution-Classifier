def solve():
    """Index: 7330.
    Returns: the time it took Pirate Rick to dig up his treasure.
    """
    # L1
    initial_sand_depth = 8 # 8 feet of sand
    initial_digging_time = 4 # 4 hours to dig up
    digging_rate = initial_sand_depth / initial_digging_time

    # L2
    storm_wash_divisor = 2 # washed away half of the sand
    sand_washed_away = initial_sand_depth / storm_wash_divisor

    # L3
    tsunami_added_sand = 2 # adding 2 feet of new sand
    final_sand_depth = initial_sand_depth - sand_washed_away + tsunami_added_sand

    # L4
    time_to_uncover = final_sand_depth / digging_rate

    # FA
    answer = time_to_uncover
    return answer