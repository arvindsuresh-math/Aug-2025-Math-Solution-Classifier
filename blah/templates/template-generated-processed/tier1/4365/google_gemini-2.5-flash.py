def solve():
    """Index: 4365.
    Returns: the total number of hits and misses in the game.
    """
    # L1
    num_times_misses_as_hits = 3 # three times as many misses as hits
    value_50_from_question = 50 # If the number of misses is 50
    calculated_misses = num_times_misses_as_hits * value_50_from_question

    # L2
    total_hits_and_misses = calculated_misses + value_50_from_question

    # FA
    answer = total_hits_and_misses
    return answer