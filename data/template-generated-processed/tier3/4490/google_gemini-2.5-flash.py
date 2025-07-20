def solve():
    """Index: 4490.
    Returns: the average number of mistakes Nadia will make.
    """
    # L1
    minutes_played = 8 # plays for 8 minutes
    notes_per_minute = 60 # can play about 60 notes a minute
    total_notes_played = minutes_played * notes_per_minute

    # L2
    notes_per_block = 40 # 3 mistakes per 40 notes
    number_of_blocks = total_notes_played / notes_per_block

    # L3
    mistakes_per_block = 3 # makes 3 mistakes per 40 notes
    total_mistakes = number_of_blocks * mistakes_per_block

    # FA
    answer = total_mistakes
    return answer