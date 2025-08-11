def solve():
    """Index: 5591.
    Returns: the number of additional days until Chris can hold his breath for 90 seconds.
    """
    # L1
    goal_seconds = 90 # 90 straight seconds
    current_seconds_day3 = 30 # On the third day, he holds it for 30 seconds
    seconds_to_improve = goal_seconds - current_seconds_day3

    # L2
    improvement_per_day = 10 # ten extra seconds each day
    days_to_reach_goal = seconds_to_improve / improvement_per_day

    # FA
    answer = days_to_reach_goal
    return answer