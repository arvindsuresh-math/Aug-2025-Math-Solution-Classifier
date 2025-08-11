def solve():
    """Index: 4670.
    Returns: the total distance the flag moved up and down the pole.
    """
    # L1
    flagpole_length = 60 # The flagpole is 60 feet long
    half_divisor = 2 # Half of the distance
    half_mast_distance = flagpole_length / half_divisor

    # L2
    total_distance_moved = flagpole_length + half_mast_distance + half_mast_distance + flagpole_length

    # FA
    answer = total_distance_moved
    return answer