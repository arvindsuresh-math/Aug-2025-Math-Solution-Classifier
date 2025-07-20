def solve():
    """Index: 4065.
    Returns: how many points their team is behind.
    """
    # L1
    max_points = 5 # Max has 5 points
    dulce_points = 3 # Dulce has 3 points
    max_dulce_combined_points = max_points + dulce_points

    # L2
    val_multiplier = 2 # twice the combined points
    val_points = max_dulce_combined_points * val_multiplier

    # L3
    team_total_points = max_dulce_combined_points + val_points

    # L4
    opponents_points = 40 # opponents' team has a total of 40 points
    points_behind = opponents_points - team_total_points

    # FA
    answer = points_behind
    return answer