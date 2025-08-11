def solve():
    """Index: 2526.
    Returns: the total distance Nate ran.
    """
    # L1
    multiplier_first_run = 4 # four times the length
    field_length = 168 # field's length is 168 meters
    distance_first_run = multiplier_first_run * field_length

    # L2
    additional_distance = 500 # ran 500 more meters
    total_distance = distance_first_run + additional_distance

    # FA
    answer = total_distance
    return answer