def solve():
    """Index: 6095.
    Returns: Beau's age today.
    """
    # L1
    sons_current_age = 16 # They are 16 years old today
    years_ago = 3 # Three years ago
    sons_age_three_years_ago = sons_current_age - years_ago

    # L2
    num_sons = 3 # 3 sons
    beau_age_three_years_ago = sons_age_three_years_ago * num_sons

    # L3
    beau_current_age = beau_age_three_years_ago + years_ago

    # FA
    answer = beau_current_age
    return answer