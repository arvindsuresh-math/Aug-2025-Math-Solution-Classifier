def solve():
    """Index: 2352.
    Returns: the total time James takes to get to Canada.
    """
    # L1
    distance = 360 # a distance of 360 miles
    speed = 60 # at 60 mph
    driving_hours = distance / speed

    # L2
    stop_hours = 1 # a 1 hour stop
    total_trip_hours = driving_hours + stop_hours

    # FA
    answer = total_trip_hours
    return answer