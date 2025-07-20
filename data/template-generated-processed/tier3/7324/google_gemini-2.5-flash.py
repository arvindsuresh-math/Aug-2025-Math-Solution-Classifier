def solve():
    """Index: 7324.
    Returns: the number of touchdowns scored by the Seattle Seahawks.
    """
    # L1
    field_goals_scored = 3 # scored 3 field goals
    points_per_field_goal = 3 # each field goal is worth 3 points
    points_from_field_goals = field_goals_scored * points_per_field_goal

    # L2
    seahawks_total_score = 37 # The final score was 37-23
    points_from_touchdowns = seahawks_total_score - points_from_field_goals

    # L3
    points_per_touchdown = 7 # a touchdown is worth 7 points
    number_of_touchdowns = points_from_touchdowns / points_per_touchdown

    # FA
    answer = number_of_touchdowns
    return answer