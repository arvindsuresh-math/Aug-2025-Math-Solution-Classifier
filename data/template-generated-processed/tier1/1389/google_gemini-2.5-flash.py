def solve():
    """Index: 1389.
    Returns: the difference in words typed before and after breaking an arm in 5 minutes.
    """
    # L1
    minutes = 5 # in 5 minutes
    wpm_before_break = 10 # type 10 words per minute
    words_before_break = minutes * wpm_before_break

    # L2
    wpm_after_break = 8 # only type 8 words per minute
    words_after_break = minutes * wpm_after_break

    # L3
    difference = words_before_break - words_after_break

    # FA
    answer = difference
    return answer