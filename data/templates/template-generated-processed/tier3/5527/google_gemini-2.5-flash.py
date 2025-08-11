def solve():
    """Index: 5527.
    Returns: the platform number David was on.
    """
    # L1
    initial_fall_depth = 4 # fell 4 meters
    additional_fall_multiplier = 3 # three more times that depth
    additional_fall_depth = additional_fall_multiplier * initial_fall_depth

    # L2
    total_fall_height = initial_fall_depth + additional_fall_depth

    # L3
    eighth_platform_number = 8 # eighth platform
    platform_height = total_fall_height / eighth_platform_number

    # L4
    david_fall_distance = 4 # fell past David after falling 4 meters
    david_height = total_fall_height - david_fall_distance

    # L5
    david_platform_number = david_height / platform_height

    # FA
    answer = david_platform_number
    return answer