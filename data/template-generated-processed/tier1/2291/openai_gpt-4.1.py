def solve():
    """Index: 2291.
    Returns: the first day Trish walks more than 10 times further than on the first day.
    """
    # L1
    first_day_distance = 1 # 1-mile walk on the first day
    double_factor = 2 # doubles the distance each day
    second_day_distance = first_day_distance * double_factor

    # L2
    third_day_distance = second_day_distance * double_factor

    # L3
    fourth_day_distance = third_day_distance * double_factor

    # L4
    fifth_day_distance = fourth_day_distance * double_factor

    # L5
    times_more = 10 # 10 times further than first day
    threshold_distance = times_more * first_day_distance

    # L6
    # She first exceeds threshold_distance on the 5th day
    answer = 5
    return answer