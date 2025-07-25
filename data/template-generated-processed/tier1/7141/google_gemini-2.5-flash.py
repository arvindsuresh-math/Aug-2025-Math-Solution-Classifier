def solve():
    """Index: 7141.
    Returns: how much longer it would take her to frost 10 cakes with her sprained wrist.
    """
    # L1
    normal_time_per_cake = 5 # Normally Ann can frost a cake in 5 minutes
    num_cakes = 10 # frost 10 cakes
    normal_total_time = normal_time_per_cake * num_cakes

    # L2
    sprained_wrist_time_per_cake = 8 # it takes her 8 minutes to frost a cake
    sprained_wrist_total_time = sprained_wrist_time_per_cake * num_cakes

    # L3
    longer_time = sprained_wrist_total_time - normal_total_time

    # FA
    answer = longer_time
    return answer