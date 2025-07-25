def solve():
    """Index: 3042.
    Returns: the average minimum speed Andy needs to drive.
    """
    # L1
    distance_slc_lv = 420 # The drive from Salt Lake City to Las Vegas is 420 miles
    distance_lv_la = 273 # The drive from Las Vegas to Los Angeles is 273 miles
    total_distance = distance_slc_lv + distance_lv_la

    # L2
    target_hours = 11 # He wants to make the drive in 11 hours
    average_speed = total_distance / target_hours

    # FA
    answer = average_speed
    return answer