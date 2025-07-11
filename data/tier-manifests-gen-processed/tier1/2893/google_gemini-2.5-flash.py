def solve():
    """Index: 2893.
    Returns: the total number of steps Raine takes walking to and from school in five days.
    """
    # L1
    steps_to_school = 150 # 150 steps to walk to the school
    round_trip_multiplier = 2 # to and from school
    steps_per_day = steps_to_school * round_trip_multiplier

    # L2
    num_days = 5 # in five days
    total_steps = steps_per_day * num_days

    # FA
    answer = total_steps
    return answer