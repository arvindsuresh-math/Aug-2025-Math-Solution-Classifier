def solve():
    """Index: 3524.
    Returns: the total weight of the entire multi-level dumbbell system.
    """
    # L1
    first_pair_weight_each = 3 # The first pair of dumbbells are 3 lb weights
    num_in_pair = 2 # WK
    first_pair_total_weight = num_in_pair * first_pair_weight_each

    # L2
    second_pair_weight_each = 5 # the second pair is 5 lb weights
    second_pair_total_weight = num_in_pair * second_pair_weight_each

    # L3
    third_pair_weight_each = 8 # the third is 8 lb pounds
    third_pair_total_weight = num_in_pair * third_pair_weight_each

    # L4
    total_system_weight = first_pair_total_weight + second_pair_total_weight + third_pair_total_weight

    # FA
    answer = total_system_weight
    return answer