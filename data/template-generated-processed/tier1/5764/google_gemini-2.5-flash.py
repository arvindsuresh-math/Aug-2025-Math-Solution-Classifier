def solve():
    """Index: 5764.
    Returns: the combined total distance the two ladies walked.
    """
    # L1
    first_lady_multiplier = 2 # twice as far
    second_lady_distance = 4 # four miles
    first_lady_distance = first_lady_multiplier * second_lady_distance

    # L2
    total_distance = second_lady_distance + first_lady_distance

    # FA
    answer = total_distance
    return answer