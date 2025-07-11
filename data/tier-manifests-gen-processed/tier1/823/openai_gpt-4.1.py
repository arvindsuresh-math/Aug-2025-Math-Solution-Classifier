def solve():
    """Index: 823.
    Returns: the number of apples left in the basket by the end of the day.
    """
    # L1
    initial_apples = 74 # 74 apples in a basket
    ricki_removes = 14 # Ricki removes 14 apples
    after_ricki = initial_apples - ricki_removes

    # L2
    samson_multiplier = 2 # twice as many as Ricki
    samson_removes = ricki_removes * samson_multiplier

    # L3
    after_samson = after_ricki - samson_removes

    # FA
    answer = after_samson
    return answer