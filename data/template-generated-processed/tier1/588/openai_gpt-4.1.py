def solve():
    """Index: 588.
    Returns: the total number of hours John worked.
    """
    # L1
    last_day = 8 # from the 3rd to the 8th, not including the 8th
    first_day = 3 # from the 3rd
    num_days = last_day - first_day

    # L2
    hours_per_day = 8 # 8 hours a day
    total_hours = num_days * hours_per_day

    # FA
    answer = total_hours
    return answer