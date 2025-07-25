def solve():
    """Index: 6497.
    Returns: the number of marbles Manny has now.
    """
    # L1
    mario_ratio_part = 4 # ratio 4:5
    manny_ratio_part = 5 # ratio 4:5
    total_ratio_parts = mario_ratio_part + manny_ratio_part

    # L2
    total_marbles = 36 # Thirty-six marbles
    marbles_per_part = total_marbles / total_ratio_parts

    # L3
    manny_initial_marbles = manny_ratio_part * marbles_per_part

    # L4
    marbles_given_away = 2 # give 2 marbles to his brother
    manny_final_marbles = manny_initial_marbles - marbles_given_away

    # FA
    answer = manny_final_marbles
    return answer