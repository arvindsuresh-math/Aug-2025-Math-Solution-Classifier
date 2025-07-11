def solve():
    """Index: 1431.
    Returns: the time the second drive will take.
    """
    # L1
    distance_first_trip = 120 # 120 miles apart
    time_first_trip = 3 # in 3 hours
    speed = distance_first_trip / time_first_trip

    # L2
    distance_second_trip = 200 # 200 miles away
    time_second_trip = distance_second_trip / speed

    # FA
    answer = time_second_trip
    return answer