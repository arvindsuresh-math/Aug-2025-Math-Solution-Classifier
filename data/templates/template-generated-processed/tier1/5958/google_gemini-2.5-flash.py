def solve():
    """Index: 5958.
    Returns: the weight Tony can lift in the squat exercise.
    """
    # L1
    curl_weight = 90 # 90 pounds with one arm in the exercise known as "the curl"
    military_press_multiplier = 2 # twice the weight that he can curl
    military_press_weight = military_press_multiplier * curl_weight

    # L2
    squat_multiplier = 5 # 5 times the weight that he can lift in the military press
    squat_weight = squat_multiplier * military_press_weight

    # FA
    answer = squat_weight
    return answer