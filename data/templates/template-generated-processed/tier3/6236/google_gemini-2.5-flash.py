def solve():
    """Index: 6236.
    Returns: the number of additional minutes needed to finish the report.
    """
    # L1
    total_words_needed = 1000 # 1000 words in length
    words_already_written = 200 # already written 200 words
    additional_words_needed = total_words_needed - words_already_written

    # L2
    words_per_half_hour = 300 # type 300 words in half an hour
    minutes_in_half_hour = 30 # WK
    words_per_minute = words_per_half_hour / minutes_in_half_hour

    # L3
    time_to_finish_minutes = additional_words_needed / words_per_minute

    # FA
    answer = time_to_finish_minutes
    return answer