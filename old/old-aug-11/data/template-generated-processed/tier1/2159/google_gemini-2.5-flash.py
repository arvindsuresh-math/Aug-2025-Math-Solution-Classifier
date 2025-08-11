def solve():
    """Index: 2159.
    Returns: the total number of minutes Marla spends on the errand.
    """
    # L1
    driving_time_one_way = 20 # 20 minutes driving one way
    round_trip_multiplier = 2 # the same amount of time driving home
    total_driving_time = driving_time_one_way * round_trip_multiplier

    # L2
    conference_time = 70 # 70 minutes attending parent-teacher night
    total_errand_time = conference_time + total_driving_time

    # FA
    answer = total_errand_time
    return answer