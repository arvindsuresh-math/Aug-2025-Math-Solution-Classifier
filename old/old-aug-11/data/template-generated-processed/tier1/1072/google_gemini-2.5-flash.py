def solve():
    """Index: 1072.
    Returns: the total number of buttons needed to manufacture all shirts.
    """
    # L1
    shirts_per_type = 200 # 200 of each type of shirt
    buttons_type1 = 3 # 3 buttons
    total_buttons_type1 = shirts_per_type * buttons_type1

    # L2
    buttons_type2 = 5 # 5 buttons
    total_buttons_type2 = shirts_per_type * buttons_type2

    # L3
    total_buttons_overall = total_buttons_type1 + total_buttons_type2

    # FA
    answer = total_buttons_overall
    return answer