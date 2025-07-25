def solve():
    """Index: 413.
    Returns: the number of green balls.
    """
    # L1
    num_blue_balls = 11 # 11 blue balls
    red_multiplier = 2 # twice as many red balls as blue
    num_red_balls = num_blue_balls * red_multiplier

    # L2
    total_red_blue_balls = num_blue_balls + num_red_balls

    # L3
    total_balls = 40 # 40 balls
    num_green_balls = total_balls - total_red_blue_balls

    # FA
    answer = num_green_balls
    return answer