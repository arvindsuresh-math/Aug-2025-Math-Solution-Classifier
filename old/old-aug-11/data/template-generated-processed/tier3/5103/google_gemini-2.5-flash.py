def solve():
    """Index: 5103.
    Returns: the number of hotdogs the 3rd competitor ate.
    """
    # L1
    first_competitor_hotdogs = 12 # 1st competitor ate 12 hot dogs
    twice_factor = 2 # twice that amount
    second_competitor_hotdogs = twice_factor * first_competitor_hotdogs

    # L2
    percentage_less_divisor = 4 # 25% less
    amount_less_for_third_competitor = second_competitor_hotdogs / percentage_less_divisor

    # L3
    third_competitor_hotdogs = second_competitor_hotdogs - amount_less_for_third_competitor

    # FA
    answer = third_competitor_hotdogs
    return answer