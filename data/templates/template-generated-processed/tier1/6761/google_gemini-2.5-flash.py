def solve():
    """Index: 6761.
    Returns: the total minutes Jill spent watching shows.
    """
    # L1
    multiplier = 4 # 4 times longer
    first_show_duration = 30 # 30 minutes long
    second_show_duration = multiplier * first_show_duration

    # L2
    total_time_spent = second_show_duration + first_show_duration

    # FA
    answer = total_time_spent
    return answer