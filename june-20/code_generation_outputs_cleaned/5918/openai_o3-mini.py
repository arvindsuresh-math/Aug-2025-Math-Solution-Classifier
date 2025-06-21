def solve(
    rise_rate: int = 50,  # the balloon would rise at a rate of 50 feet per minute
    descend_rate: int = 10,  # the balloon would slowly descend at a rate of 10 feet per minute
    pull_time1: int = 15,  # pulled the chain for 15 minutes
    release_time: int = 10,  # released the chain for 10 minutes
    pull_time2: int = 15   # pulled the chain for another 15 minutes
):
    """Index: 5918.
    Returns: the highest elevation reached by the balloon.
    """
    #: L1
    ascent_first_pull = rise_rate * pull_time1   # 50*15 = 750 feet
    #: L2
    descent_during_release = descend_rate * release_time  # 10*10 = 100 feet
    #: L3
    ascent_second_pull = rise_rate * pull_time2   # 50*15 = 750 feet
    #: L4
    highest_elevation = ascent_first_pull - descent_during_release + ascent_second_pull  # 750-100+750 = 1400 feet

    answer = highest_elevation  # FINAL ANSWER
    return answer