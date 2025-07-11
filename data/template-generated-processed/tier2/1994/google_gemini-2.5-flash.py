def solve():
    """Index: 1994.
    Returns: the total number of fruits left.
    """
    # L1
    oranges_count = 40 # 40 oranges
    apples_count = 70 # 70 apples
    total_initial_fruits = oranges_count + apples_count

    # L2
    oranges_sold_fraction_decimal = 0.25 # 1/4 of the oranges
    oranges_sold = oranges_count * oranges_sold_fraction_decimal

    # L3
    apples_sold_fraction_decimal = 0.50 # 1/2 of the apples
    apples_sold = apples_count * apples_sold_fraction_decimal

    # L4
    fruits_left = total_initial_fruits - oranges_sold - apples_sold

    # FA
    answer = fruits_left
    return answer