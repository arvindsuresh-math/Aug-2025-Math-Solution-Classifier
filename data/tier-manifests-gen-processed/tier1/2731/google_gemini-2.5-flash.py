def solve():
    """Index: 2731.
    Returns: the number of laps Jeff had remaining when he took the break.
    """
    # L1
    total_laps_required = 98 # swim 98 laps over the weekend
    laps_swam_saturday = 27 # swam 27 laps
    remaining_after_saturday = total_laps_required - laps_swam_saturday

    # L2
    laps_swam_sunday_morning = 15 # swam 15 laps
    remaining_after_sunday_morning = remaining_after_saturday - laps_swam_sunday_morning

    # FA
    answer = remaining_after_sunday_morning
    return answer