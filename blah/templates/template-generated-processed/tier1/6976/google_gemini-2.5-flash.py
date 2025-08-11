def solve():
    """Index: 6976.
    Returns: the number of seashells in a month.
    """
    # L1
    current_week_seashells = 50 # 50 seashells in the jar this week
    increase_per_week = 20 # 20 more seashells
    seashells_week_1 = current_week_seashells + increase_per_week

    # L2
    seashells_week_2 = seashells_week_1 + increase_per_week

    # L3
    seashells_week_3 = seashells_week_2 + increase_per_week

    # L4
    seashells_week_4 = seashells_week_3 + increase_per_week

    # FA
    answer = seashells_week_4
    return answer