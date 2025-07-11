def solve():
    """Index: 1761.
    Returns: the number of passion fruit crates Kevin sold.
    """
    # L1
    grapes_crates = 13 # 13 crates of grapes
    mangoes_crates = 20 # 20 crates of mangoes
    other_fruits_total = grapes_crates + mangoes_crates

    # L2
    total_crates_per_week = 50 # total of 50 crates of fruit per week
    passion_fruit_crates = total_crates_per_week - other_fruits_total

    # FA
    answer = passion_fruit_crates
    return answer