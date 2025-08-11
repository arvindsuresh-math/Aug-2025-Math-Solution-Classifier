def solve():
    """Index: 6334.
    Returns: the number of hours Jaydee will take to finish typing the research paper.
    """
    # L1
    total_words = 4560 # research paper with 4560 words
    words_per_minute = 38 # type 38 words in a minute
    minutes_to_type = total_words / words_per_minute

    # L2
    minutes_per_hour = 60 # WK
    hours_to_finish = minutes_to_type / minutes_per_hour

    # FA
    answer = hours_to_finish
    return answer