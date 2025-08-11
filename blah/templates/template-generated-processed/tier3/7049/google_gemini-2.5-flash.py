def solve():
    """Index: 7049.
    Returns: the difference in the number of water breaks and sitting breaks James takes.
    """
    # L1
    total_work_minutes = 240 # James works for 240 minutes
    water_break_interval = 20 # takes a water break every 20 minutes
    num_water_breaks = total_work_minutes / water_break_interval

    # L2
    sitting_break_interval = 120 # a sitting break every 120 minutes
    num_sitting_breaks = total_work_minutes / sitting_break_interval

    # L3
    difference_in_breaks = num_water_breaks - num_sitting_breaks

    # FA
    answer = difference_in_breaks
    return answer