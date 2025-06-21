def solve(
    rise_rate: int = 50, # rise at a rate of 50 feet per minute
    descend_rate: int = 10, # descend at a rate of 10 feet per minute
    first_pull_duration: int = 15, # pulled the chain for 15 minutes
    first_release_duration: int = 10, # released the rope for 10 minutes
    second_pull_duration: int = 15 # pulled the chain for another 15 minutes
):
    """Index: 5918.
    Returns: the highest elevation reached by the balloon.
    """
    #: L1
    first_rise = rise_rate * first_pull_duration

    #: L2
    first_descent = descend_rate * first_release_duration

    #: L3
    second_rise = rise_rate * second_pull_duration

    #: L4
    highest_elevation = first_rise - first_descent + second_rise

    answer = highest_elevation # FINAL ANSWER
    return answer