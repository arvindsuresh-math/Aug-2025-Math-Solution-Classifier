def solve():
    """Index: 1761.
    Returns: the number of passion fruit crates Kevin sold last week.
    """
    # L1
    grapes_crates = 13 # 13 crates of grapes
    mangoes_crates = 20 # 20 crates of mangoes
    grapes_and_mangoes = grapes_crates + mangoes_crates

    # L2
    total_crates = 50 # sells a total of 50 crates of fruit per week
    passion_fruit_crates = total_crates - grapes_and_mangoes

    # FA
    answer = passion_fruit_crates
    return answer