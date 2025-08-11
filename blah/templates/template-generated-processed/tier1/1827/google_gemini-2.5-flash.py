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
    eggs_for_self = 2 # 2 eggs for herself
    total_eggs_per_breakfast = eggs_for_husband + eggs_for_self + eggs_for_children

    # L3
    days_per_week_breakfast = 5 # Monday through Friday
    weeks_per_year = 52 # WK
    total_breakfasts_per_year = days_per_week_breakfast * weeks_per_year

    # L4
    total_eggs_per_year = total_eggs_per_breakfast * total_breakfasts_per_year

    # FA
    answer = total_eggs_per_year
    return answer