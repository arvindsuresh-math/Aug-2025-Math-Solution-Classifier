def solve():
    """Index: 4734.
    Returns: the total number of chairs in the classroom.
    """
    # L1
    blue_chairs = 10 # 10 blue chairs
    green_multiplier = 3 # 3 times as many as the blue chairs
    green_chairs = blue_chairs * green_multiplier

    # L2
    blue_green_combined = blue_chairs + green_chairs

    # L3
    white_chairs_fewer = 13 # 13 fewer white chairs
    white_chairs = blue_green_combined - white_chairs_fewer

    # L4
    total_chairs = blue_green_combined + white_chairs

    # FA
    answer = total_chairs
    return answer