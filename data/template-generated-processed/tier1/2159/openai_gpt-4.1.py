def solve():
    """Index: 2159.
    Returns: the total number of minutes Marla spends on the errand.
    """
    # L1
    one_way_drive = 20 # 20 minutes driving one way
    num_trips = 2 # driving to and from school
    total_drive = one_way_drive * num_trips

    # L2
    conference_time = 70 # 70 minutes attending parent-teacher night
    total_time = conference_time + total_drive

    # FA
    answer = total_time
    return answer