def solve(
    rise_rate: int = 50,  # balloon rises at 50 feet per minute when chain is pulled
    first_pull_duration: int = 15,  # first chain pull duration in minutes
    descend_rate: int = 10,  # balloon descends at 10 feet per minute when chain is released
    first_release_duration: int = 10,  # first chain release duration in minutes
    second_pull_duration: int = 15  # second chain pull duration in minutes
):
    """Index: 5918.
    Returns: the highest elevation reached by the balloon during the ride.
    """
    #: L1
    first_rise = rise_rate * first_pull_duration

    #: L2
    first_descent = descend_rate * first_release_duration

    #: L3
    second_rise = rise_rate * second_pull_duration

    #: L4
    highest_elevation = first_rise - first_descent + second_rise

    answer = highest_elevation  # FINAL ANSWER
    return answer