def solve():
    """Index: 7052.
    Returns: the total miles Felix will cover.
    """
    # L1
    average_speed_mph = 66 # 66 miles per hour
    speed_multiplier = 2 # twice as fast
    new_speed_mph = speed_multiplier * average_speed_mph

    # L2
    drive_time_hours = 4 # 4 hours
    total_miles_covered = new_speed_mph * drive_time_hours

    # FA
    answer = total_miles_covered
    return answer