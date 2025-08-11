def solve():
    """Index: 103.
    Returns: the number of sentences Janice started with today.
    """
    # L2
    sentences_per_minute = 6 # Janice can type 6 sentences per minute
    minutes_before_break = 20 # typed for 20 minutes
    sentences_before_break = sentences_per_minute * minutes_before_break

    # L3
    minutes_after_break = 15 # typed 15 minutes longer
    sentences_after_break = sentences_per_minute * minutes_after_break

    # L4
    minutes_after_meeting = 18 # typed for 18 minutes more
    sentences_after_meeting = sentences_per_minute * minutes_after_meeting

    # L5
    total_sentences_typed = sentences_before_break + sentences_after_break + sentences_after_meeting

    # L6
    sentences_erased = 40 # had to erase 40 sentences
    sentences_typed_left = total_sentences_typed - sentences_erased

    # L7 (no computation, just sets up the equation)
    # L8
    sentences_at_end = 536 # paper had 536 sentences by the end of today
    sentences_started_with = sentences_at_end - sentences_typed_left

    # FA
    answer = sentences_started_with
    return answer