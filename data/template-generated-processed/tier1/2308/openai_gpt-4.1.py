def solve():
    """Index: 2308.
    Returns: the number of bandages left in the box after Peggy finished putting bandages on her knees.
    """
    # L1
    dozen = 12 # WK
    num_dozens = 2 # two dozen bandages
    two_dozen = dozen * num_dozens

    # L2
    less_than = 8 # 8 less than two dozen
    initial_bandages = two_dozen - less_than

    # L3
    left_knee_bandages = 2 # two bandages on her left knee
    right_knee_bandages = 3 # three bandages on her right knee
    total_used = left_knee_bandages + right_knee_bandages

    # L4
    bandages_remaining = initial_bandages - total_used

    # FA
    answer = bandages_remaining
    return answer