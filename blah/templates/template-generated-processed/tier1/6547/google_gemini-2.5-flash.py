def solve():
    """Index: 6547.
    Returns: the total number of buttons Sally needs to sew all the shirts.
    """
    # L1
    shirts_monday = 4 # 4 shirts on Monday
    shirts_tuesday = 3 # 3 shirts on Tuesday
    shirts_wednesday = 2 # 2 shirts on Wednesday
    total_shirts = shirts_monday + shirts_tuesday + shirts_wednesday

    # L2
    buttons_per_shirt = 5 # 5 buttons
    total_buttons_needed = total_shirts * buttons_per_shirt

    # FA
    answer = total_buttons_needed
    return answer