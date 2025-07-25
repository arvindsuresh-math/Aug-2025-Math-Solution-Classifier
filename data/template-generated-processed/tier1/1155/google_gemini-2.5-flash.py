def solve():
    """Index: 1155.
    Returns: the time it took Gloria's turtle to finish the race.
    """
    # L1
    greta_time = 6 # Greta’s turtle finished the race in 6 minutes
    george_quicker_minutes = 2 # 2 minutes quicker than Greta’s
    george_time = greta_time - george_quicker_minutes

    # L2
    twice_multiplier = 2 # took twice as long
    gloria_time = twice_multiplier * george_time

    # FA
    answer = gloria_time
    return answer