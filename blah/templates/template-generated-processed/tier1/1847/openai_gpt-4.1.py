def solve():
    """Index: 1847.
    Returns: the number of bottles of juice left after the week.
    """
    # L1
    bottles_refrigerator = 4 # 4 bottles of juice in the refrigerator
    bottles_pantry = 4 # 4 bottles of juice in the pantry
    initial_bottles = bottles_refrigerator + bottles_pantry

    # L2
    bottles_bought = 5 # Martha bought 5 more bottles of juice
    total_bottles = bottles_bought + initial_bottles

    # L3
    bottles_drank = 3 # Martha and her family drank 3 bottles of juice during the week
    bottles_left = total_bottles - bottles_drank

    # FA
    answer = bottles_left
    return answer