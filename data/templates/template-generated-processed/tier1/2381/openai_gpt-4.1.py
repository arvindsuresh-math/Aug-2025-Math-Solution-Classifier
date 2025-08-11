def solve():
    """Index: 2381.
    Returns: the total number of balls in the box Clive opens.
    """
    # L1
    blue_balls = 6 # 6 blue balls
    green_multiplier = 3 # 3 times as many green balls as blue ones
    green_balls = blue_balls * green_multiplier

    # L2
    red_balls = 4 # 4 red balls
    yellow_multiplier = 2 # twice as many yellow ones as red ones
    yellow_balls = red_balls * yellow_multiplier

    # L3
    total_balls = blue_balls + red_balls + green_balls + yellow_balls

    # FA
    answer = total_balls
    return answer