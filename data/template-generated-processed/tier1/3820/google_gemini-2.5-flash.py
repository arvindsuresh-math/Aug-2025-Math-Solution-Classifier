def solve():
    """Index: 3820.
    Returns: the total time it takes to get ready.
    """
    # L1
    jack_shoes_time = 4 # 4 minutes to put his shoes on
    extra_time_per_toddler = 3 # three minutes longer to help each toddler
    time_per_toddler = jack_shoes_time + extra_time_per_toddler

    # L2
    num_toddlers = 2 # both his toddlers
    total_toddler_time = time_per_toddler * num_toddlers

    # L3
    total_time = total_toddler_time + jack_shoes_time

    # FA
    answer = total_time
    return answer