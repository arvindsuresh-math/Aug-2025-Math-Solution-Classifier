def solve():
    """Index: 1918.
    Returns: the height the ball will bounce on the fifth bounce.
    """
    # L1
    initial_height = 96 # 96-foot tall building
    bounce_factor = 2 # half the height
    height_bounce_1 = initial_height / bounce_factor

    # L2
    height_bounce_2 = height_bounce_1 / bounce_factor

    # L3
    height_bounce_3 = height_bounce_2 / bounce_factor

    # L4
    height_bounce_4 = height_bounce_3 / bounce_factor

    # L5
    height_bounce_5 = height_bounce_4 / bounce_factor

    # FA
    answer = height_bounce_5
    return answer