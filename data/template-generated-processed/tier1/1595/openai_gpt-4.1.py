def solve():
    """Index: 1595.
    Returns: how many more points the Fireflies scored than the Hornets in the game.
    """
    # L1
    fireflies_3pt_baskets = 7 # Fireflies scored 7 three-point baskets
    points_per_3pt = 3 # 3-point baskets
    fireflies_points_final_seconds = fireflies_3pt_baskets * points_per_3pt

    # L2
    fireflies_initial_score = 74 # Fireflies had 74 points
    fireflies_final_score = fireflies_initial_score + fireflies_points_final_seconds

    # L3
    hornets_2pt_baskets = 2 # Hornets scored 2 two-point baskets
    points_per_2pt = 2 # 2-point baskets
    hornets_points_final_seconds = hornets_2pt_baskets * points_per_2pt

    # L4
    hornets_initial_score = 86 # Hornets had 86 points
    hornets_final_score = hornets_initial_score + hornets_points_final_seconds

    # L5
    point_difference = fireflies_final_score - hornets_final_score

    # FA
    answer = point_difference
    return answer