def solve():
    """Index: 972.
    Returns: the number of floors in the building.
    """
    # L1
    start_floor = 9 # on the 9th floor
    down_1 = 7 # goes down 7 floors
    after_down = start_floor - down_1

    # L2
    up_1 = 3 # then up 3 floors
    after_up1 = after_down + up_1

    # L3
    up_2 = 8 # then up 8 floors
    top_floor = after_up1 + up_2

    # FA
    answer = top_floor
    return answer