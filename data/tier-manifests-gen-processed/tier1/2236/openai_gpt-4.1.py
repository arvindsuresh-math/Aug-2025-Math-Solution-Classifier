def solve():
    """Index: 2236.
    Returns: the number of seashells Evie has left after giving 2 to her brother.
    """
    # L1
    shells_per_day = 10 # collects her favorite 10 shells
    num_days = 6 # at the end of 6 days
    total_shells = shells_per_day * num_days

    # L2
    shells_given = 2 # gives 2 shells to her brother
    shells_left = total_shells - shells_given

    # FA
    answer = shells_left
    return answer