def solve():
    """Index: 3885.
    Returns: the total points James scored.
    """
    # L1
    field_goal_value = 3 # 3 points
    num_field_goals = 13 # 13 field goals
    field_goal_points = field_goal_value * num_field_goals

    # L2
    two_point_shot_value = 2 # two points
    num_two_point_shots = 20 # 20 shots
    two_point_shot_points = two_point_shot_value * num_two_point_shots

    # L3
    total_score = field_goal_points + two_point_shot_points

    # FA
    answer = total_score
    return answer