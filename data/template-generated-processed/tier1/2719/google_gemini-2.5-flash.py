def solve():
    """Index: 2719.
    Returns: the total hours it will take to make all of the bread.
    """
    # L1
    num_balls_dough = 4 # 4 balls of dough
    rise_time_per_ball = 3 # 3 hours to rise 1 ball of dough
    total_rise_time = num_balls_dough * rise_time_per_ball

    # L2
    bake_time_per_ball = 2 # another 2 hours to bake it
    total_bake_time = num_balls_dough * bake_time_per_ball

    # L3
    total_time = total_rise_time + total_bake_time

    # FA
    answer = total_time
    return answer