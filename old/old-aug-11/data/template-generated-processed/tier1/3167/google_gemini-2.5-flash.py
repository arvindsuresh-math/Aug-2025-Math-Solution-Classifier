def solve():
    """Index: 3167.
    Returns: the total time in minutes they took to inflate all the soccer balls.
    """
    # L1
    time_per_ball = 20 # twenty minutes to inflate
    alexia_balls = 20 # Alexia inflating 20 balls
    alexia_time = time_per_ball * alexia_balls

    # L2
    ermias_extra_balls = 5 # 5 more balls than Alexia
    ermias_balls = alexia_balls + ermias_extra_balls

    # L3
    ermias_time = ermias_balls * time_per_ball

    # L4
    total_time = alexia_time + ermias_time

    # FA
    answer = total_time
    return answer