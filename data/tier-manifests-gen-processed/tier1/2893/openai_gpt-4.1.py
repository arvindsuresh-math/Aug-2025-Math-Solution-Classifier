def solve():
    """Index: 2893.
    Returns: the total number of steps Raine takes walking to and from school in five days.
    """
    # L1
    steps_one_way = 150 # it takes her 150 steps to walk to the school
    trips_per_day = 2 # to and from school each day
    steps_per_day = steps_one_way * trips_per_day

    # L2
    num_days = 5 # in five days
    total_steps = steps_per_day * num_days

    # FA
    answer = total_steps
    return answer