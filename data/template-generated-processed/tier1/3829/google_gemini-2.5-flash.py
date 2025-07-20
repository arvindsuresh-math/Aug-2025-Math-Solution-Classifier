def solve():
    """Index: 3829.
    Returns: the difference between the number of tangerines and oranges left.
    """
    # L1
    initial_oranges = 5 # 5 oranges
    oranges_taken_away = 2 # took away 2 oranges
    oranges_left = initial_oranges - oranges_taken_away

    # L2
    initial_tangerines = 17 # 17 tangerines
    tangerines_taken_away = 10 # took away 10 tangerines
    tangerines_left = initial_tangerines - tangerines_taken_away

    # L3
    difference_tangerines_oranges = tangerines_left - oranges_left

    # FA
    answer = difference_tangerines_oranges
    return answer