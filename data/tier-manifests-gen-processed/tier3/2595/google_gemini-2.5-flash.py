def solve():
    """Index: 2595.
    Returns: the average number of goals Xavier can score.
    """
    # L1
    match_duration_hours = 2 # 2 hours
    minutes_per_hour = 60 # WK
    total_minutes = match_duration_hours * minutes_per_hour

    # L2
    time_per_goal_group = 15 # 15 minutes Xavier can score 2 goals
    number_of_groups = total_minutes / time_per_goal_group

    # L3
    goals_per_group = 2 # score 2 goals on average
    average_goals = number_of_groups * goals_per_group

    # FA
    answer = average_goals
    return answer