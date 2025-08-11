def solve():
    """Index: 1642.
    Returns: the total number of pages filled by the essays.
    """
    # L1
    johnny_words = 150 # Johnny wrote an essay with 150 words
    double_factor = 2 # double in length
    madeline_words = johnny_words * double_factor

    # L2
    additional_timothy_words = 30 # had 30 words more than Madeline's
    timothy_words = madeline_words + additional_timothy_words

    # L3
    total_words = johnny_words + madeline_words + timothy_words

    # L4
    words_per_page = 260 # one page contains 260 words
    total_pages = total_words / words_per_page

    # FA
    answer = total_pages
    return answer