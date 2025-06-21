def solve(
    flagpole_length: int = 60 # The flagpole is 60 feet long
):
    """Index: 4670.
    Returns: the total distance in feet the flag moved up and down the pole during the day.
    """
    #: L1
    half_flagpole = flagpole_length / 2

    #: L2
    total_distance = flagpole_length + half_flagpole + half_flagpole + flagpole_length

    answer = total_distance # FINAL ANSWER
    return answer