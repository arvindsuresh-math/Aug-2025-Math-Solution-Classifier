def solve():
    """Index: 1288.
    Returns: the total time James spends on his chores.
    """
    # L1
    vacuuming_hours = 3 # 3 hours vacuuming
    multiplier_other_chores = 3 # 3 times as long on the rest of his chores
    other_chores_hours = vacuuming_hours * multiplier_other_chores

    # L2
    total_chores_hours = vacuuming_hours + other_chores_hours

    # FA
    answer = total_chores_hours
    return answer