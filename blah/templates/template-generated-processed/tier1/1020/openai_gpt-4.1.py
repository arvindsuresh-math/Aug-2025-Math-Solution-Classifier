def solve():
    """Index: 1020.
    Returns: how many more words Matt writes in 5 minutes with his right hand than with his left.
    """
    # L1
    right_hand_wpm = 10 # 10 words a minute with his right hand
    left_hand_wpm = 7 # 7 words a minute with his left hand
    speed_difference = right_hand_wpm - left_hand_wpm

    # L2
    minutes = 5 # 5 minutes
    more_words = speed_difference * minutes

    # FA
    answer = more_words
    return answer