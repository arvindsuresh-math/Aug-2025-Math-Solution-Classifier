def solve():
    """Index: 3357.
    Returns: the number of tennis balls in each container.
    """
    # L1
    total_tennis_balls = 100 # 100 tennis balls
    half_divisor = 2 # gives half of them away
    tennis_balls_kept = total_tennis_balls / half_divisor

    # L2
    num_containers = 5 # puts into 5 large containers
    balls_per_container = tennis_balls_kept / num_containers

    # FA
    answer = balls_per_container
    return answer