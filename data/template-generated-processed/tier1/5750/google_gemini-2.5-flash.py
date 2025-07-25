def solve():
    """Index: 5750.
    Returns: the total number of fruits that Sophie and Hannah had eaten in the 30 days.
    """
    # L1
    sophie_oranges_per_day = 20 # 20 oranges every day
    num_days = 30 # for 30 days
    sophie_total_oranges = sophie_oranges_per_day * num_days

    # L2
    hannah_grapes_per_day = 40 # 40 grapes every day
    hannah_total_grapes = hannah_grapes_per_day * num_days

    # L3
    total_fruits = hannah_total_grapes + sophie_total_oranges

    # FA
    answer = total_fruits
    return answer