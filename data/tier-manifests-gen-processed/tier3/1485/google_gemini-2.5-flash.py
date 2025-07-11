def solve():
    """Index: 1485.
    Returns: the number of orange balls.
    """
    # L1
    total_balls = 50 # Adam has 50 balls
    red_balls = 20 # 20 balls are red
    blue_balls = 10 # 10 are blue
    pink_and_orange_balls = total_balls - red_balls - blue_balls

    # L3
    orange_balls_coefficient = 1 # WK
    pink_balls_multiplier = 3 # 3 times as many pink as orange balls
    combined_coefficient = orange_balls_coefficient + pink_balls_multiplier

    # L4
    orange_balls = pink_and_orange_balls / combined_coefficient

    # FA
    answer = orange_balls
    return answer