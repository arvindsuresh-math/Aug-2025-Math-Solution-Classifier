def solve():
    """Index: 727.
    Returns: the total number of shells Shara has now.
    """
    # L1
    shells_per_day = 5 # 5 shells per day
    num_days_initial = 3 # 3 days
    shells_found_initial_days = shells_per_day * num_days_initial

    # L2
    shells_fourth_day = 6 # 6 shells on the fourth day
    total_shells_vacation = shells_found_initial_days + shells_fourth_day

    # L3
    initial_shells = 20 # 20 shells before she went on vacation
    total_shells_now = initial_shells + total_shells_vacation

    # FA
    answer = total_shells_now
    return answer