def solve():
    """Index: 5582.
    Returns: the height of the 101st floor.
    """
    # L1
    num_floors_1_to_100 = 100 # first to 100th floors
    height_per_floor_1_to_100 = 16.5 # height each equal to 16.5 feet
    height_floors_1_to_100 = num_floors_1_to_100 * height_per_floor_1_to_100

    # L2
    total_height_taipei_101 = 1673 # 1,673 feet tall
    height_101st_floor = total_height_taipei_101 - height_floors_1_to_100

    # FA
    answer = height_101st_floor
    return answer