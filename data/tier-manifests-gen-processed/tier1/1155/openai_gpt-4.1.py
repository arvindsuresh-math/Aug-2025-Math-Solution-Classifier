def solve():
    """Index: 1155.
    Returns: the time it took Gloria's turtle to finish the race in minutes.
    """
    # L1
    greta_time = 6 # Greta’s turtle finished the race in 6 minutes
    george_quicker = 2 # George’s turtle finished 2 minutes quicker than Greta’s
    george_time = greta_time - george_quicker

    # L2
    gloria_multiplier = 2 # Gloria’s turtle took twice as long as George’s turtle
    gloria_time = gloria_multiplier * george_time

    # FA
    answer = gloria_time
    return answer