def solve():
    """Index: 5309.
    Returns: the total time students spend outside of class.
    """
    # L1
    num_breaks_15_min = 2 # 2 15-minute recess breaks
    duration_break_15_min = 15 # 15-minute recess breaks
    total_15_min_breaks = num_breaks_15_min * duration_break_15_min

    # L2
    lunch_duration = 30 # a 30-minute lunch
    recess_duration_20_min = 20 # another 20-minute recess break
    total_time_outside_class = lunch_duration + recess_duration_20_min + total_15_min_breaks

    # FA
    answer = total_time_outside_class
    return answer