def solve():
    """Index: 6426.
    Returns: the number of 50-segment millipedes needed.
    """
    # L1
    segments_initial_millipede = 60 # one millipede with 60 segments
    twice_factor = 2 # twice as long
    segments_per_long_millipede = segments_initial_millipede * twice_factor

    # L2
    number_of_long_millipedes = 2 # 2 millipedes that are twice as long
    total_segments_from_long_millipedes = segments_per_long_millipede * number_of_long_millipedes

    # L3
    total_segments_eaten = segments_initial_millipede + total_segments_from_long_millipedes

    # L4
    daily_segment_goal = 800 # a total of 800 body segments every day
    segments_still_needed = daily_segment_goal - total_segments_eaten

    # L5
    segments_per_new_millipede = 50 # 50-segment millipedes
    num_new_millipedes_needed = segments_still_needed / segments_per_new_millipede

    # FA
    answer = num_new_millipedes_needed
    return answer