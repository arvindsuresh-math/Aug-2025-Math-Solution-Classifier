def solve():
    """Index: 690.
    Returns: the number of bottles remaining in Jose's cellar.
    """
    # L1
    imported_wine_bottles = 2400 # 2400 bottles of imported wine
    domestic_wine_divisor = 2 # half as many bottles of domestic wine as imported wine
    domestic_wine_bottles = imported_wine_bottles / domestic_wine_divisor

    # L2
    total_wine_bottles = imported_wine_bottles + domestic_wine_bottles

    # L3
    consumed_divisor = 3 # one-third of all his wine
    consumed_bottles = total_wine_bottles / consumed_divisor

    # L4
    remaining_bottles = total_wine_bottles - consumed_bottles

    # FA
    answer = remaining_bottles
    return answer