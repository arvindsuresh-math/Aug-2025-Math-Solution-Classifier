def solve():
    """Index: 1994.
    Returns: the total number of fruits Tom has left after selling some oranges and apples.
    """
    # L1
    oranges = 40 # Tom got 40 oranges
    apples = 70 # Tom got 70 apples
    total_fruits = oranges + apples

    # L2
    oranges_fraction_sold = 0.25 # sold 1/4 of the oranges
    oranges_sold = oranges * oranges_fraction_sold

    # L3
    apples_fraction_sold = 0.50 # sold 1/2 of the apples
    apples_sold = apples * apples_fraction_sold

    # L4
    fruits_left = total_fruits - oranges_sold - apples_sold

    # FA
    answer = fruits_left
    return answer