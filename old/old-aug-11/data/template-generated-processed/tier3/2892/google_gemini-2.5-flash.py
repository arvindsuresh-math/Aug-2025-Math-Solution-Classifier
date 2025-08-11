def solve():
    """Index: 2892.
    Returns: the speed in mph above the speed limit John was driving.
    """
    # L1
    distance = 150 # John travels 150 miles
    time = 2 # in 2 hours
    johns_speed = distance / time

    # L2
    speed_limit = 60 # The speed limit is 60 mph
    speed_above_limit = johns_speed - speed_limit

    # FA
    answer = speed_above_limit
    return answer