def solve():
    """Index: 5592.
    Returns: the cost per tennis ball.
    """
    # L1
    num_packs = 4 # 4 packs of tennis balls
    balls_per_pack = 3 # 3 balls per pack
    total_balls = num_packs * balls_per_pack

    # L2
    total_cost = 24 # $24 in total
    cost_per_ball = total_cost / total_balls

    # FA
    answer = cost_per_ball
    return answer