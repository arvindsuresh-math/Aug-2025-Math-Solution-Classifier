def solve():
    """Index: 4491.
    Returns: the total number of buttons Jack must use.
    """
    # L1
    num_kids = 3 # 3 kids
    shirts_per_kid = 3 # 3 shirts for each of his 3 kids
    total_shirts = num_kids * shirts_per_kid

    # L2
    buttons_per_shirt = 7 # 7 buttons in each shirt
    total_buttons = total_shirts * buttons_per_shirt

    # FA
    answer = total_buttons
    return answer