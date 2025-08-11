def solve():
    """Index: 4100.
    Returns: the distance in miles between consecutive checkpoints.
    """
    # L1
    total_marathon_length = 26 # A 26-mile circular marathon
    distance_from_start = 1 # The first is one mile from the start line
    distance_from_finish = 1 # and the last checkpoint is one mile from the finish line
    effective_spacing_length = total_marathon_length - distance_from_start - distance_from_finish

    # L2
    num_checkpoints = 4 # has four checkpoints
    distance_between_checkpoints = effective_spacing_length / num_checkpoints

    # FA
    answer = distance_between_checkpoints
    return answer