def solve():
    """Index: 4264.
    Returns: the percentage of the team's total points Marcus scored.
    """
    # L1
    three_point_goals = 5 # 5 3-point goals
    points_per_three_point_goal = 3 # 3-point goals
    marcus_three_point_score = three_point_goals * points_per_three_point_goal

    # L2
    two_point_goals = 10 # 10 2-point goals
    points_per_two_point_goal = 2 # 2-point goals
    marcus_two_point_score = two_point_goals * points_per_two_point_goal

    # L3
    marcus_total_score = marcus_three_point_score + marcus_two_point_score

    # L4
    team_total_points = 70 # team scored 70 points overall
    percentage_multiplier = 100 # 100%
    marcus_percentage_of_team_score = (marcus_total_score / team_total_points) * percentage_multiplier

    # FA
    answer = marcus_percentage_of_team_score
    return answer