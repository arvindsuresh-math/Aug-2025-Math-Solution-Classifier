def solve():
    """Index: 2529.
    Returns: the number of hotdogs the third competitor can eat after 5 minutes.
    """
    # L1
    first_competitor_rate = 10 # 10 hot dogs per minute
    second_competitor_multiplier = 3 # 3 times more than the first competitor
    second_competitor_rate = first_competitor_rate * second_competitor_multiplier

    # L2
    third_competitor_multiplier = 2 # twice as much as the second competitor
    third_competitor_rate = second_competitor_rate * third_competitor_multiplier

    # L3
    time_minutes = 5 # after 5 minutes
    total_hotdogs_third_competitor = third_competitor_rate * time_minutes

    # FA
    answer = total_hotdogs_third_competitor
    return answer