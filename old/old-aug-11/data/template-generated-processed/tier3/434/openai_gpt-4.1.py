def solve():
    """Index: 434.
    Returns: the percentage Calvin is towards his haircut goal.
    """
    # L1
    haircuts_so_far = 8 # he has gotten 8 haircuts
    haircuts_remaining = 2 # needs 2 more to reach his goal
    total_goal_haircuts = haircuts_so_far + haircuts_remaining

    # L2
    percent_multiplier = 100 # WK
    percent_towards_goal = (haircuts_so_far / total_goal_haircuts) * percent_multiplier

    # FA
    answer = percent_towards_goal
    return answer