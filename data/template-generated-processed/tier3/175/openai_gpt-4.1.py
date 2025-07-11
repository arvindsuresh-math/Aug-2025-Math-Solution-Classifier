def solve():
    """Index: 175.
    Returns: the average speed of Conner's dune buggy in miles per hour.
    """
    # L1
    flat_speed = 60 # it can ride at a speed of 60 miles per hour
    downhill_increase = 12 # 12 miles per hour faster than it can when it is on flat sand
    downhill_speed = flat_speed + downhill_increase

    # L2
    uphill_decrease = 18 # 18 miles per hour slower than when it is riding on flat sand
    uphill_speed = flat_speed - uphill_decrease

    # L3
    time_fraction = 3 # one-third of the time on each
    average_speed = (flat_speed + downhill_speed + uphill_speed) / time_fraction

    # FA
    answer = average_speed
    return answer