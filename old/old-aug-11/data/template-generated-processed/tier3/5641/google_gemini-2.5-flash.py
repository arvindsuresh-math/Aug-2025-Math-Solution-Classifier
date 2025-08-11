def solve():
    """Index: 5641.
    Returns: the number of hours before the deadline Keenan needs to start.
    """
    # L1
    words_per_hour_initial = 400 # writes 400 words per hour
    initial_hours = 2 # for the first two hours
    words_written_initial = words_per_hour_initial * initial_hours

    # L2
    total_words_needed = 1200 # essay that is 1200 words
    remaining_words = total_words_needed - words_written_initial

    # L3
    words_per_hour_after = 200 # she writes 200 words per hour
    hours_for_remaining_words = remaining_words / words_per_hour_after

    # L4
    total_hours_needed = initial_hours + hours_for_remaining_words

    # FA
    answer = total_hours_needed
    return answer