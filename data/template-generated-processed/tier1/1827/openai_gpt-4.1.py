def solve():
    """Index: 1827.
    Returns: the total number of eggs Lisa cooks for her family for breakfast in a year.
    """
    # L1
    eggs_per_child = 2 # 2 eggs for each of her 4 children
    num_children = 4 # 4 children
    eggs_for_children = eggs_per_child * num_children

    # L2
    eggs_for_husband = 3 # 3 eggs for her husband
    eggs_for_lisa = 2 # 2 eggs for herself
    eggs_per_breakfast = eggs_for_husband + eggs_for_lisa + eggs_for_children

    # L3
    days_per_week = 5 # every morning, Monday through Friday
    weeks_per_year = 52 # WK
    num_breakfasts = days_per_week * weeks_per_year

    # L4
    total_eggs = eggs_per_breakfast * num_breakfasts

    # FA
    answer = total_eggs
    return answer