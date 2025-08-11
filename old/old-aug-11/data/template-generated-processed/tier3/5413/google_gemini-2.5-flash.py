def solve():
    """Index: 5413.
    Returns: the time in minutes Ben would take to pick the target number of peas.
    """
    # L1
    total_peas_L1 = 56 # 56 sugar snap peas
    time_to_pick_L1 = 7 # seven minutes
    peas_per_minute = total_peas_L1 / time_to_pick_L1

    # L2
    target_peas = 72 # 72 sugar snap peas
    time_to_pick_target_peas = target_peas / peas_per_minute

    # FA
    answer = time_to_pick_target_peas
    return answer