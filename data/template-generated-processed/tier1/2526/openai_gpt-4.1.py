def solve():
    """Index: 2526.
    Returns: the total distance Nate ran in meters.
    """
    # L1
    multiplier = 4 # four times the length of a football field
    field_length = 168 # field's length is 168 meters
    first_run = multiplier * field_length

    # L2
    second_run = 500 # ran 500 more meters
    total_distance = first_run + second_run

    # FA
    answer = total_distance
    return answer