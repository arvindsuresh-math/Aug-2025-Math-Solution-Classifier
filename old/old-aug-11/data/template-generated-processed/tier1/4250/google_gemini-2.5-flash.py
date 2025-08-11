def solve():
    """Index: 4250.
    Returns: the total number of chairs taken to the hall.
    """
    # L1
    num_friends = 4 # four friends
    kingsley = 1 # Kingsley herself
    total_students = num_friends + kingsley

    # L2
    num_trips = 10 # 10 trips in total
    chairs_per_trip = 5 # 5 chairs per trip
    chairs_per_student = num_trips * chairs_per_trip

    # L3
    total_chairs = chairs_per_student * total_students

    # FA
    answer = total_chairs
    return answer