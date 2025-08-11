def solve():
    """Index: 1706.
    Returns: the number of students who play soccer.
    """
    # L1
    total_students = 400 # 400 students in the senior class
    percent_play_sports = 0.52 # 52% of the students play sports
    num_play_sports = total_students * percent_play_sports

    # L2
    percent_play_soccer = 0.125 # 12.5% play soccer
    num_play_soccer = num_play_sports * percent_play_soccer

    # FA
    answer = num_play_soccer
    return answer