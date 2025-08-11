def solve():
    """Index: 1389.
    Returns: the difference in the number of words Cameron could type in 5 minutes before and after he broke his arm.
    """
    # L1
    minutes = 5 # in 5 minutes
    wpm_before = 10 # 10 words per minute before
    words_before = minutes * wpm_before

    # L2
    wpm_after = 8 # 8 words per minute after
    words_after = minutes * wpm_after

    # L3
    difference = words_before - words_after

    # FA
    answer = difference
    return answer