def solve():
    """Index: 1160.
    Returns: how much longer it would take Julia to run 5 miles in her new shoes than if she wore her old ones.
    """
    # L1
    miles_to_run = 5 # 5 miles
    normal_mile_time = 10 # 10 minutes
    time_with_normal_shoes = miles_to_run * normal_mile_time

    # L2
    new_shoes_mile_time = 13 # 13 minutes
    time_with_new_shoes = new_shoes_mile_time * miles_to_run

    # L3
    time_difference = time_with_new_shoes - time_with_normal_shoes

    # FA
    answer = time_difference
    return answer