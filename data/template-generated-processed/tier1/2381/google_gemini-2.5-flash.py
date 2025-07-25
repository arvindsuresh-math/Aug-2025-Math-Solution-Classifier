def solve():
    """Index: 2381.
    Returns: the total number of balls in the box.
    """
    # L1
    num_blue_balls = 6 # 6 blue balls
    green_multiplier = 3 # 3 times as many green balls as blue ones
    num_green_balls = num_blue_balls * green_multiplier

    # L2
    num_red_balls = 4 # 4 red balls
    yellow_multiplier = 2 # twice as many yellow ones as red ones
    num_yellow_balls = num_red_balls * yellow_multiplier

    # L3
    total_balls = num_blue_balls + num_red_balls + num_green_balls + num_yellow_balls

    # FA
    answer = total_balls
    return answer