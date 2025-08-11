def solve():
    """Index: 4827.
    Returns: the number of balls that are neither red nor blue.
    """
    # L1
    total_balls = 360 # 360 balls in the ball pit
    red_fraction_numerator = 1 # a quarter of the balls
    red_fraction_denominator = 4 # a quarter of the balls
    red_balls = total_balls * (red_fraction_numerator / red_fraction_denominator)

    # L2
    remaining_balls_after_red = total_balls - red_balls

    # L3
    blue_fraction_numerator = 1 # a fifth of the remaining balls
    blue_fraction_denominator = 5 # a fifth of the remaining balls
    blue_balls = remaining_balls_after_red * (blue_fraction_numerator / blue_fraction_denominator)

    # L4
    total_red_and_blue_balls = red_balls + blue_balls

    # L5
    neither_red_nor_blue_balls = total_balls - total_red_and_blue_balls

    # FA
    answer = neither_red_nor_blue_balls
    return answer