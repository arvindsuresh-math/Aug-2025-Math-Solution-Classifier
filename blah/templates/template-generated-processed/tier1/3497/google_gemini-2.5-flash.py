def solve():
    """Index: 3497.
    Returns: the total time it takes both of them to run all around the two arenas.
    """
    # L1
    emma_time = 20 # Emma can run all-around two arenas in 20 hours
    fernando_multiplier = 2 # takes Fernando twice as long
    fernando_time = fernando_multiplier * emma_time

    # L2
    total_time = fernando_time + emma_time

    # FA
    answer = total_time
    return answer