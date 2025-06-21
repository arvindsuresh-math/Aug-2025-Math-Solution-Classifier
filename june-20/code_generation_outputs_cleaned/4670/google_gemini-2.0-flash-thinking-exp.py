def solve(
    flagpole_length: int = 60 # The flagpole is 60 feet long
):
    """Index: 4670.
    Returns: the total distance the flag moved up and down the pole over the course of the day.
    """
    #: L1
    half_mast_distance = flagpole_length / 2

    #: L2
    total_distance_moved = flagpole_length + half_mast_distance + half_mast_distance + flagpole_length

    answer = total_distance_moved # FINAL ANSWER
    return answer