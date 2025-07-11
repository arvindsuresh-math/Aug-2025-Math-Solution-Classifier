def solve():
    """Index: 444.
    Returns: the number of points Reggie loses by.
    """
    # L1
    reggie_layups = 3 # Reggie makes 3 layups
    layup_points = 1 # Layups are worth 1 point
    reggie_layup_score = reggie_layups * layup_points

    # L2
    reggie_free_throws = 2 # two free throws
    free_throw_points = 2 # free throws are worth 2 points
    reggie_free_throw_score = reggie_free_throws * free_throw_points

    # L3
    reggie_long_shots = 1 # one long shot
    long_shot_points = 3 # anything further away is worth 3 points
    reggie_long_shot_score = reggie_long_shots * long_shot_points

    # L4
    reggie_total = reggie_layup_score + reggie_free_throw_score + reggie_long_shot_score

    # L5
    brother_long_shots = 4 # makes 4 of them
    brother_score = brother_long_shots * long_shot_points

    # L6
    reggie_loses_by = brother_score - reggie_total

    # FA
    answer = reggie_loses_by
    return answer