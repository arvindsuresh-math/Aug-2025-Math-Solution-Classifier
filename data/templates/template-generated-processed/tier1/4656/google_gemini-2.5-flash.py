def solve():
    """Index: 4656.
    Returns: the total number of fruits Mary has left.
    """
    # L1
    initial_apples = 14 # 14 apples
    ate_one_of_each = 1 # ate 1 of each
    apples_left = initial_apples - ate_one_of_each

    # L2
    initial_oranges = 9 # 9 oranges
    oranges_left = initial_oranges - ate_one_of_each

    # L3
    initial_blueberries = 6 # 6 blueberries
    blueberries_left = initial_blueberries - ate_one_of_each

    # L4
    total_fruits_left = apples_left + oranges_left + blueberries_left

    # FA
    answer = total_fruits_left
    return answer