def solve():
    """Index: 588.
    Returns: the total number of hours John worked.
    """
    # L1
    end_day = 8 # 8th
    start_day = 3 # 3rd
    days_worked = end_day - start_day

    # L2
    hours_per_day = 8 # 8 hours a day
    total_hours_worked = days_worked * hours_per_day

    # FA
    answer = total_hours_worked
    return answer