def solve():
    """Index: 1847.
    Returns: the number of bottles of juice left.
    """
    # L1
    bottles_in_pantry = 4 # 4 bottles in the pantry
    bottles_in_refrigerator = 4 # 4 bottles of juice in the refrigerator
    initial_bottles = bottles_in_pantry + bottles_in_refrigerator

    # L2
    bought_more_bottles = 5 # bought 5 more bottles of juice
    bottles_after_shopping = bought_more_bottles + initial_bottles

    # L3
    drank_bottles = 3 # drank 3 bottles of juice
    bottles_left = bottles_after_shopping - drank_bottles

    # FA
    answer = bottles_left
    return answer