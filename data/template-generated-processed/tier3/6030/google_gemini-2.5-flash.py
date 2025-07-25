def solve():
    """Index: 6030.
    Returns: the additional distance the car will travel.
    """
    # L1
    distance_initial = 180 # traveled 180 miles
    time_initial = 4 # in 4 hours
    average_speed = distance_initial / time_initial

    # L2
    time_next = 3 # in the next 3 hours
    distance_next = average_speed * time_next

    # FA
    answer = distance_next
    return answer