def solve():
    """Index: 4574.
    Returns: the number of notebooks Amanda has now.
    """
    # L1
    ordered_this_week = 6 # ordered 6 more
    lost_this_week = 2 # lost 2
    net_change_this_week = ordered_this_week - lost_this_week

    # L2
    initial_notebooks = 10 # had 10 notebooks
    final_notebooks = initial_notebooks + net_change_this_week

    # FA
    answer = final_notebooks
    return answer