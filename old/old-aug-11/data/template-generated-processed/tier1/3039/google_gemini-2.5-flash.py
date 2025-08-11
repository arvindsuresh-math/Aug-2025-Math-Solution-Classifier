def solve():
    """Index: 3039.
    Returns: the minimum current load the transformer must be able to carry.
    """
    # L1
    num_units = 3 # three units of machinery
    running_current_per_unit = 40 # running current of 40A each
    total_running_current = num_units * running_current_per_unit

    # L2
    starting_current_multiplier = 2 # at least twice their running current for starting
    minimum_current_load = starting_current_multiplier * total_running_current

    # FA
    answer = minimum_current_load
    return answer