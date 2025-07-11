def solve():
    """Index: 972.
    Returns: the total number of floors in the building.
    """
    # L1
    initial_floor = 9 # on the 9th floor
    down_floors_1 = 7 # goes down 7 floors
    floor_after_down_1 = initial_floor - down_floors_1

    # L2
    up_floors_1 = 3 # then up 3 floors
    floor_after_up_1 = floor_after_down_1 + up_floors_1

    # L3
    up_floors_2 = 8 # then up 8 floors
    final_floor = floor_after_up_1 + up_floors_2

    # FA
    answer = final_floor
    return answer