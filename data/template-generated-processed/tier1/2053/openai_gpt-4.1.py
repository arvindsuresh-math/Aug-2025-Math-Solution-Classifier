def solve():
    """Index: 2053.
    Returns: the total number of apples Adam collected from his orchard.
    """
    # L1
    apples_per_day = 4 # picks 4 apples from his orchard
    num_days = 30 # every day for 30 days
    apples_first_period = apples_per_day * num_days

    # L2
    remaining_apples = 230 # all the remaining apples, which were 230
    total_apples = apples_first_period + remaining_apples

    # FA
    answer = total_apples
    return answer