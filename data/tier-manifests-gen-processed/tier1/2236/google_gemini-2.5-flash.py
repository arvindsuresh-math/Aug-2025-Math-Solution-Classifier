def solve():
    """Index: 2236.
    Returns: the number of shells Evie has left.
    """
    # L1
    shells_per_day = 10 # 10 shells
    num_days = 6 # At the end of 6 days
    total_shells_collected = shells_per_day * num_days

    # L2
    shells_given_to_brother = 2 # gives 2 shells to her brother
    shells_left = total_shells_collected - shells_given_to_brother

    # FA
    answer = shells_left
    return answer