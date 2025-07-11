def solve():
    """Index: 413.
    Returns: the number of green balls Ryan has.
    """
    # L1
    blue_balls = 11 # If there are 11 blue balls
    red_to_blue_ratio = 2 # twice as many red balls as blue
    red_balls = blue_balls * red_to_blue_ratio

    # L2
    blue_and_red_total = blue_balls + red_balls

    # L3
    total_balls = 40 # Ryan has 40 balls
    green_balls = total_balls - blue_and_red_total

    # FA
    answer = green_balls
    return answer