def solve():
    """Index: 7186.
    Returns: the total duration of the commercial break in minutes.
    """
    # L1
    num_5_min_commercials = 3 # three 5-minute commercials
    duration_5_min_commercial = 5 # 5-minute commercials
    total_5_min_commercials_duration = num_5_min_commercials * duration_5_min_commercial

    # L2
    duration_2_min_commercial = 2 # 2-minute commercials
    num_2_min_commercials = 11 # eleven 2-minute commercials
    total_2_min_commercials_duration = duration_2_min_commercial * num_2_min_commercials

    # L3
    total_commercial_break_duration = total_5_min_commercials_duration + total_2_min_commercials_duration

    # FA
    answer = total_commercial_break_duration
    return answer