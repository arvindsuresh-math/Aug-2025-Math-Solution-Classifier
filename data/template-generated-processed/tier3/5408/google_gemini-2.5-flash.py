def solve():
    """Index: 5408.
    Returns: the total number of peanuts Darma could eat.
    """
    # L1
    seconds_per_minute = 60 # WK
    minutes = 6 # 6 minutes
    total_seconds = seconds_per_minute * minutes

    # L2
    time_per_set_seconds = 15 # 15 seconds
    num_sets = total_seconds / time_per_set_seconds

    # L3
    peanuts_per_set = 20 # 20 peanuts
    total_peanuts = num_sets * peanuts_per_set

    # FA
    answer = total_peanuts
    return answer