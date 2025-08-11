def solve():
    """Index: 3013.
    Returns: the total weight John moves.
    """
    # L1
    weight_per_rep = 15 # 15 pounds
    reps_per_set = 10 # 10 reps
    weight_per_set = weight_per_rep * reps_per_set

    # L2
    num_sets = 3 # 3 sets
    total_weight_moved = num_sets * weight_per_set

    # FA
    answer = total_weight_moved
    return answer