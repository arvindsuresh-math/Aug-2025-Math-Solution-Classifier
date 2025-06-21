def solve(
    flagpole_length: int = 60  # "The flagpole is 60 feet long"
):
    """Index: 4670.
    Returns: the total distance the flag moved up and down the pole in feet.
    """
    #: L1
    half_distance = flagpole_length // 2  # 60/2 = 30 feet

    #: L2
    total_distance = flagpole_length + half_distance + half_distance + flagpole_length  # 60 up + 30 down + 30 up + 60 down

    answer = total_distance  # FINAL ANSWER
    return answer