def solve():
    """Index: 3741.
    Returns: the number of minutes it will take Roger to reach his goal.
    """
    # L1
    minutes_for_2000_steps = 30 # 30 minutes
    steps_in_30_minutes = 2000 # 2,000 steps
    minutes_per_step = minutes_for_2000_steps / steps_in_30_minutes

    # L2
    goal_steps = 10000 # 10,000 steps
    total_minutes_to_goal = minutes_per_step * goal_steps

    # FA
    answer = total_minutes_to_goal
    return answer