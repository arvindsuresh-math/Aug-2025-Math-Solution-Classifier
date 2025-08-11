def solve():
    """Index: 1020.
    Returns: the number of more words Matt would write with his right hand than with his left in 5 minutes.
    """
    # L1
    right_hand_wpm = 10 # 10 words a minute with his right hand
    left_hand_wpm = 7 # 7 words a minute with his left hand
    speed_difference = right_hand_wpm - left_hand_wpm

    # L2
    time_minutes = 5 # in 5 minutes
    total_difference_words = speed_difference * time_minutes

    # FA
    answer = total_difference_words
    return answer