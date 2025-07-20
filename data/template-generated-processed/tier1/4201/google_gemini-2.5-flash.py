def solve():
    """Index: 4201.
    Returns: the total number of points the team scored in the fourth quarter.
    """
    # L1
    losing_team_first_quarter_points = 10 # the losing team had 10 points in the first quarter
    double_multiplier = 2 # double the points
    winning_team_first_quarter_points = losing_team_first_quarter_points * double_multiplier

    # L2
    points_added_second_quarter = 10 # had 10 more points
    winning_team_second_quarter_points = winning_team_first_quarter_points + points_added_second_quarter

    # L3
    points_added_third_quarter = 20 # had 20 more points
    winning_team_third_quarter_points = points_added_third_quarter + winning_team_second_quarter_points

    # L4
    total_game_points = 80 # total points the winning team scored in the game was 80
    fourth_quarter_points = total_game_points - winning_team_third_quarter_points

    # FA
    answer = fourth_quarter_points
    return answer