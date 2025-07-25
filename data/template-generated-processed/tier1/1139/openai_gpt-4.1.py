def solve():
    """Index: 1139.
    Returns: the total number of balls in the fish tank.
    """
    # L1
    num_goldfish = 3 # three goldfish
    red_balls_per_goldfish = 10 # each goldfish plays with ten red balls
    num_red_balls = num_goldfish * red_balls_per_goldfish

    # L2
    num_platyfish = 10 # ten platyfish
    white_balls_per_platyfish = 5 # each platyfish plays with five white balls
    num_white_balls = num_platyfish * white_balls_per_platyfish

    # L3
    total_balls = num_white_balls + num_red_balls

    # FA
    answer = total_balls
    return answer