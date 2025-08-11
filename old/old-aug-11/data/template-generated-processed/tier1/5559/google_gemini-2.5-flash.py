def solve():
    """Index: 5559.
    Returns: the total points Lemuel made in the game.
    """
    # L1
    points_per_shot_2 = 2 # 2-point shots
    times_made_2_point = 7 # made 2-point shots 7 times
    points_from_2_point_shots = points_per_shot_2 * times_made_2_point

    # L2
    points_per_shot_3 = 3 # 3-points shots
    times_made_3_point = 3 # made 3-points shots thrice
    points_from_3_point_shots = points_per_shot_3 * times_made_3_point

    # L3
    total_points = points_from_2_point_shots + points_from_3_point_shots

    # FA
    answer = total_points
    return answer