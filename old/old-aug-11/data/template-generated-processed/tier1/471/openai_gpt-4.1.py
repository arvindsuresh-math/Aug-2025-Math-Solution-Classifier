def solve():
    """Index: 471.
    Returns: the total number of floors in the building.
    """
    # L1
    start_floor = 1 # first floor
    up1 = 5 # went up 5 floors
    after_up1 = start_floor + up1

    # L2
    down1 = 2 # went down 2 floors
    after_down1 = after_up1 - down1

    # L3
    up2 = 7 # went up 7 floors
    after_up2 = after_down1 + up2

    # L4
    floors_away_from_top = 9 # 9 floors away from the top
    total_floors = after_up2 + floors_away_from_top

    # FA
    answer = total_floors
    return answer