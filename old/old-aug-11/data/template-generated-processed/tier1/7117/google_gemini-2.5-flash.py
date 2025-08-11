def solve():
    """Index: 7117.
    Returns: the time it took Jack to run up the second half of the hill.
    """
    # L1
    jill_total_time = 32 # Jill finished the race in 32 seconds
    jack_time_before_jill = 7 # 7 seconds before Jill did
    jack_total_time = jill_total_time - jack_time_before_jill

    # L2
    jack_first_half_time = 19 # Jack ran up the first half of the hill in 19 seconds
    jack_second_half_time = jack_total_time - jack_first_half_time

    # FA
    answer = jack_second_half_time
    return answer