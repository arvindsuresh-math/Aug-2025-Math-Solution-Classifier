def solve():
    """Index: 1595.
    Returns: the difference in points between the Fireflies and the Hornets at the end of the game.
    """
    # L1
    fireflies_three_point_baskets = 7 # 7 three-point baskets
    points_per_three_point_basket = 3 # 3-point baskets
    fireflies_points_from_baskets = points_per_three_point_basket * fireflies_three_point_baskets

    # L2
    fireflies_initial_score = 74 # score of 86 to 74
    fireflies_final_score = fireflies_initial_score + fireflies_points_from_baskets

    # L3
    hornets_two_point_baskets = 2 # 2 two-point baskets
    points_per_two_point_basket = 2 # 2-point baskets
    hornets_points_from_baskets = points_per_two_point_basket * hornets_two_point_baskets

    # L4
    hornets_initial_score = 86 # score of 86 to 74
    hornets_final_score = hornets_initial_score + hornets_points_from_baskets

    # L5
    final_difference = fireflies_final_score - hornets_final_score

    # FA
    answer = final_difference
    return answer