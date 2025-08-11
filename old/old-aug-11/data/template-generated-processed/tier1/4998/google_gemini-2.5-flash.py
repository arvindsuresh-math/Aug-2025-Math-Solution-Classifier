def solve():
    """Index: 4998.
    Returns: Tabitha's current age.
    """
    # L1
    colors_in_future = 8 # 8 different colors in her hair
    years_from_now = 3 # In three years
    current_colors = colors_in_future - years_from_now

    # L2
    colors_at_15 = 2 # 2 colors in her hair
    age_at_2_colors = 15 # 15 years old
    colors_added_since_15 = current_colors - colors_at_15

    # L3
    years_added = colors_added_since_15

    # L4
    current_age = age_at_2_colors + years_added

    # FA
    answer = current_age
    return answer