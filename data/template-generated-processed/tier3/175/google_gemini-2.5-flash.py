def solve():
    """Index: 175.
    Returns: the average speed of the dune buggy in miles per hour.
    """
    # L1
    flat_sand_speed = 60 # speed of 60 miles per hour
    downhill_speed_increase = 12 # 12 miles per hour faster
    downhill_speed = flat_sand_speed + downhill_speed_increase

    # L2
    uphill_speed_decrease = 18 # 18 miles per hour slower
    uphill_speed = flat_sand_speed - uphill_speed_decrease

    # L3
    time_fraction_denominator = 3 # one-third of the time
    average_speed = (flat_sand_speed + downhill_speed + uphill_speed) / time_fraction_denominator

    # FA
    answer = average_speed
    return answer