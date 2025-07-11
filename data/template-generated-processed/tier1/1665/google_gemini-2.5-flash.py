def solve():
    """Index: 1665.
    Returns: the number of yellow balls Jamie bought.
    """
    # L1
    red_balls_initial = 16 # 16 red balls
    blue_multiplier = 2 # two times more blue balls
    blue_balls_initial = blue_multiplier * red_balls_initial

    # L2
    red_balls_lost = 6 # lost 6 of the red balls
    red_balls_after_loss = red_balls_initial - red_balls_lost

    # L3
    total_red_blue_balls = blue_balls_initial + red_balls_after_loss

    # L4
    total_balls_final = 74 # 74 balls in total
    yellow_balls_bought = total_balls_final - total_red_blue_balls

    # FA
    answer = yellow_balls_bought
    return answer