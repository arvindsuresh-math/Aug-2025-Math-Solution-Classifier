def solve():
    """Index: 471.
    Returns: the total number of floors in the building.
    """
    # L1
    start_floor = 1 # first floor
    up_5_floors = 5 # went up 5 floors
    current_floor_after_up_5 = start_floor + up_5_floors

    # L2
    down_2_floors = 2 # went down 2 floors
    current_floor_after_down_2 = current_floor_after_up_5 - down_2_floors

    # L3
    up_7_floors = 7 # went up 7 floors
    current_floor_after_up_7 = current_floor_after_down_2 + up_7_floors

    # L4
    floors_away_from_top = 9 # 9 floors away from the top of the building
    total_floors = current_floor_after_up_7 + floors_away_from_top

    # FA
    answer = total_floors
    return answer