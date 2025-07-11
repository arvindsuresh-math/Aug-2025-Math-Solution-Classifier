def solve():
    """Index: 2308.
    Returns: the number of bandages left in the box.
    """
    # L1
    dozen = 12 # WK
    num_of_dozens = 2 # two dozen bandages
    initial_total_from_dozens = dozen * num_of_dozens

    # L2
    less_amount = 8 # 8 less than two dozen bandages
    bandages_before_peggy = initial_total_from_dozens - less_amount

    # L3
    left_knee_bandages = 2 # two bandages on her left knee
    right_knee_bandages = 3 # three bandages on her right knee
    total_bandages_needed = left_knee_bandages + right_knee_bandages

    # L4
    bandages_remaining = bandages_before_peggy - total_bandages_needed

    # FA
    answer = bandages_remaining
    return answer