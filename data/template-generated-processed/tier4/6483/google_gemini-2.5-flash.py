def solve():
    """Index: 6483.
    Returns: the number of cups of turnips Carrie can add.
    """
    # L1
    potatoes_initial = 5 # 5 cups of potatoes
    turnips_initial = 2 # 2 cups of turnips
    potato_to_turnip_ratio = potatoes_initial / turnips_initial

    # L2
    potatoes_current = 20 # 20 cups of potatoes
    turnips_to_add = potatoes_current / potato_to_turnip_ratio

    # FA
    answer = turnips_to_add
    return answer