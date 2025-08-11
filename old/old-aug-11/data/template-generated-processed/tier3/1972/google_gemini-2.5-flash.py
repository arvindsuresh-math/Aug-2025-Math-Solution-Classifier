def solve():
    """Index: 1972.
    Returns: the difference in weight between the largest and smallest frog.
    """
    # L1
    largest_frog_weight = 120 # The largest frog weighs 120 pounds
    weight_multiple = 10 # 10 times as much
    smallest_frog_weight = largest_frog_weight / weight_multiple

    # L2
    weight_difference = largest_frog_weight - smallest_frog_weight

    # FA
    answer = weight_difference
    return answer