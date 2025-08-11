def solve():
    """Index: 444.
    Returns: the number of points Reggie loses by.
    """
    # L1
    reggie_layups_made = 3 # Reggie makes 3 layups
    layup_points_value = 1 # Layups are worth 1 point
    reggie_layup_points = reggie_layups_made * layup_points_value

    # L2
    reggie_free_throws_made = 2 # two free throws
    free_throw_points_value = 2 # free throws are worth 2 points
    reggie_free_throw_points = reggie_free_throws_made * free_throw_points_value

    # L3
    reggie_long_shots_made = 1 # one long shot
    long_shot_points_value = 3 # anything further away is worth 3 points
    reggie_long_shot_points = reggie_long_shots_made * long_shot_points_value

    # L4
    reggie_total_points = reggie_layup_points + reggie_free_throw_points + reggie_long_shot_points

    # L5
    brother_long_shots_made = 4 # makes 4 of them
    brother_total_points = brother_long_shots_made * long_shot_points_value

    # L6
    points_reggie_loses_by = brother_total_points - reggie_total_points

    # FA
    answer = points_reggie_loses_by
    return answer