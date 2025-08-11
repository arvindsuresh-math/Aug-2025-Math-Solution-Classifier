def solve():
    """Index: 5262.
    Returns: the number of additional hours Fabian needed to walk.
    """
    # L1
    total_distance_needed = 30 # a total of 30 kilometers
    speed_km_per_hour = 5 # Every hour he covers 5 kilometers
    total_hours_needed = total_distance_needed / speed_km_per_hour

    # L2
    hours_already_walked = 3 # walked there for 3 hours
    additional_hours_needed = total_hours_needed - hours_already_walked

    # FA
    answer = additional_hours_needed
    return answer