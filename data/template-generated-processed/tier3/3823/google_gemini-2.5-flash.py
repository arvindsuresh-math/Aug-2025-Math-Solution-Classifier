def solve():
    """Index: 3823.
    Returns: the total kilograms of garbage accumulated.
    """
    # L2
    average_garbage_per_collection = 200 # an average of 200 kg is taken
    collection_days_per_week = 3 # Tuesdays, Thursdays, and Saturdays
    garbage_first_week = average_garbage_per_collection * collection_days_per_week

    # L3
    reduction_factor_second_week = 2 # cutting their amount of garbage in half
    garbage_second_week = garbage_first_week / reduction_factor_second_week

    # L4
    total_garbage_accumulated = garbage_first_week + garbage_second_week

    # FA
    answer = total_garbage_accumulated
    return answer