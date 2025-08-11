def solve():
    """Index: 6000.
    Returns: the time it will take 6 builders to build the cottage.
    """
    # L1
    days_for_3_builders = 8 # 8 days for 3 builders
    initial_builders = 3 # 3 builders
    days_for_one_builder = days_for_3_builders * initial_builders

    # L2
    target_builders = 6 # 6 builders
    days_for_6_builders = days_for_one_builder / target_builders

    # FA
    answer = days_for_6_builders
    return answer