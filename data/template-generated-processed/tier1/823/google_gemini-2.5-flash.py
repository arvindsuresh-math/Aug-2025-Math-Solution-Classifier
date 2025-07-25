def solve():
    """Index: 823.
    Returns: the number of apples left in the basket by the end of the day.
    """
    # L1
    initial_apples = 74 # 74 apples in a basket
    ricki_removes = 14 # Ricki removes 14 apples
    apples_after_ricki = initial_apples - ricki_removes

    # L2
    multiplier_samson = 2 # twice as many as Ricki
    samson_removes = ricki_removes * multiplier_samson

    # L3
    apples_after_samson = apples_after_ricki - samson_removes

    # FA
    answer = apples_after_samson
    return answer