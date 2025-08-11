def solve():
    """Index: 3122.
    Returns: the total number of baskets made during the game.
    """
    # L1
    matthew_score = 9 # Matthew scored 9 points
    points_per_basket = 3 # Each basket was worth 3 points
    matthew_baskets = matthew_score / points_per_basket

    # L2
    shawn_score = 6 # Shawn scored 6 points
    shawn_baskets = shawn_score / points_per_basket

    # L3
    total_baskets = matthew_baskets + shawn_baskets

    # FA
    answer = total_baskets
    return answer