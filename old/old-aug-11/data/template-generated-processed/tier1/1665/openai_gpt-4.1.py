def solve():
    """Index: 1665.
    Returns: the number of yellow balls Jamie bought.
    """
    # L1
    red_balls_initial = 16 # He had 16 red balls
    blue_to_red_ratio = 2 # two times more blue balls
    blue_balls = blue_to_red_ratio * red_balls_initial

    # L2
    red_balls_lost = 6 # he lost 6 of the red balls
    red_balls_remaining = red_balls_initial - red_balls_lost

    # L3
    total_red_blue = blue_balls + red_balls_remaining

    # L4
    total_balls_after = 74 # he had 74 balls in total
    yellow_balls = total_balls_after - total_red_blue

    # FA
    answer = yellow_balls
    return answer