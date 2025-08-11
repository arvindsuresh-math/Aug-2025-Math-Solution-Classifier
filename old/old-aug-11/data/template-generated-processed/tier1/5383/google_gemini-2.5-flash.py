def solve():
    """Index: 5383.
    Returns: the number of bundles of wood burned in the afternoon.
    """
    # L1
    bundles_start_day = 10 # 10 bundles of wood at the start of the day
    bundles_end_day = 3 # 3 bundles of wood at the end of the day
    bundles_burned_total = bundles_start_day - bundles_end_day

    # L2
    bundles_burned_morning = 4 # burns 4 bundles of wood in the morning
    bundles_burned_afternoon = bundles_burned_total - bundles_burned_morning

    # FA
    answer = bundles_burned_afternoon
    return answer