def solve():
    """Index: 233.
    Returns: the total number of push-ups Bryan did.
    """
    # L1
    num_sets = 3 # 3 sets
    pushups_per_set = 15 # 15 push-ups each
    total_pushups_if_all = num_sets * pushups_per_set

    # L2
    fewer_pushups_third_set = 5 # does 5 fewer push-ups
    total_pushups = total_pushups_if_all - fewer_pushups_third_set

    # FA
    answer = total_pushups
    return answer