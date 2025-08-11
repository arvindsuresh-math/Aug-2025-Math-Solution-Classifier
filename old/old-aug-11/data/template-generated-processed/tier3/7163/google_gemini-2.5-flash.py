def solve():
    """Index: 7163.
    Returns: the difference in time between the second route and the first route.
    """
    # L1
    uphill_walk_time = 6 # walks for 6 minutes uphill
    path_multiplier = 2 # twice this amount of time
    path_walk_time = uphill_walk_time * path_multiplier

    # L2
    first_two_stages_time = uphill_walk_time + path_walk_time

    # L3
    final_stage_divisor = 3 # a third of the time
    final_stage_time = first_two_stages_time / final_stage_divisor

    # L4
    total_first_route_time = first_two_stages_time + final_stage_time

    # L5
    flat_path_time = 14 # walks along a flat path for 14 minutes
    second_stage_multiplier = 2 # twice this amount of time
    second_route_second_stage_time = flat_path_time * second_stage_multiplier

    # L6
    total_second_route_time = second_route_second_stage_time + flat_path_time

    # L7
    time_difference = total_second_route_time - total_first_route_time

    # FA
    answer = time_difference
    return answer