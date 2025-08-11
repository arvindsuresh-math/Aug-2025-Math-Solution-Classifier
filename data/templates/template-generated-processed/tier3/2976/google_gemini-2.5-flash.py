def solve():
    """Index: 2976.
    Returns: the total number of fences Abigail would have built.
    """
    # L1
    hours_to_build = 8 # for the next 8 hours
    minutes_per_hour = 60 # WK
    total_minutes_building = hours_to_build * minutes_per_hour

    # L2
    minutes_per_fence = 30 # Each fence took her 30 minutes to build
    fences_built_in_additional_hours = total_minutes_building / minutes_per_fence

    # L3
    initial_fences_built = 10 # Abigail built 10 fences
    total_fences_built = initial_fences_built + fences_built_in_additional_hours

    # FA
    answer = total_fences_built
    return answer