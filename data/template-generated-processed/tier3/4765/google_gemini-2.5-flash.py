def solve():
    """Index: 4765.
    Returns: the total time Javier spends on his speech.
    """
    # L1
    outlining_time = 30 # 30 minutes outlining his speech
    additional_writing_time = 28 # 28 more minutes writing than outlining
    writing_time = outlining_time + additional_writing_time

    # L2
    divisor_for_practicing = 2 # half as much time practicing as writing
    practicing_time = writing_time / divisor_for_practicing

    # L3
    total_time = practicing_time + writing_time + outlining_time

    # FA
    answer = total_time
    return answer