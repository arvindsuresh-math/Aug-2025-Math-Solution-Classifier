def solve():
    """Index: 233.
    Returns: the total number of push-ups Bryan did.
    """
    # L1
    num_sets = 3 # 3 sets
    pushups_per_set = 15 # 15 push-ups each
    total_planned_pushups = num_sets * pushups_per_set

    # L2
    fewer_pushups = 5 # 5 fewer push-ups
    actual_total_pushups = total_planned_pushups - fewer_pushups

    # FA
    answer = actual_total_pushups
    return answer