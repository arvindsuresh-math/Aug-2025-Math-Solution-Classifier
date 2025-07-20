def solve():
    """Index: 7249.
    Returns: the number of words Vinnie has exceeded the limit by.
    """
    # L1
    words_saturday = 450 # 450 words on Saturday
    words_sunday = 650 # 650 words on Sunday
    total_words_written = words_saturday + words_sunday

    # L2
    word_limit = 1000 # 1000-word limit
    words_exceeded = total_words_written - word_limit

    # FA
    answer = words_exceeded
    return answer