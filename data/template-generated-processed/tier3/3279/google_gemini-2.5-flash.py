def solve():
    """Index: 3279.
    Returns: the time it takes for one kid to wash six whiteboards.
    """
    # L1
    time_initial = 20 # 20 minutes
    num_kids_initial = 4 # Four kids
    time_one_kid_three_boards = time_initial * num_kids_initial

    # L2
    num_whiteboards_target = 6 # six whiteboards
    num_whiteboards_initial = 3 # three whiteboards
    time_one_kid_six_boards = time_one_kid_three_boards * (num_whiteboards_target / num_whiteboards_initial)

    # FA
    answer = time_one_kid_six_boards
    return answer