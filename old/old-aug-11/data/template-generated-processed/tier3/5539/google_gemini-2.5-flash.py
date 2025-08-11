def solve():
    """Index: 5539.
    Returns: the total time Monica spent studying during the five days.
    """
    # L1
    wednesday_hours = 2 # studied for 2 hours on Wednesday
    thursday_multiplier = 3 # three times as long on Thursday
    thursday_hours = thursday_multiplier * wednesday_hours

    # L2
    friday_divisor = 2 # half of the time she studied on Thursday
    friday_hours = thursday_hours / friday_divisor

    # L3
    total_before_weekend = wednesday_hours + thursday_hours + friday_hours

    # L4
    total_study_time = total_before_weekend + total_before_weekend

    # FA
    answer = total_study_time
    return answer