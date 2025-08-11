def solve():
    """Index: 2529.
    Returns: the number of hotdogs the third competitor can eat after 5 minutes.
    """
    # L1
    first_hotdogs_per_min = 10 # first competitor can eat 10 hot dogs per minute
    second_multiplier = 3 # 3 times more than the first competitor
    second_hotdogs_per_min = first_hotdogs_per_min * second_multiplier

    # L2
    third_multiplier = 2 # twice as much as the second competitor
    third_hotdogs_per_min = second_hotdogs_per_min * third_multiplier

    # L3
    minutes = 5 # after 5 minutes
    third_total_hotdogs = third_hotdogs_per_min * minutes

    # FA
    answer = third_total_hotdogs
    return answer