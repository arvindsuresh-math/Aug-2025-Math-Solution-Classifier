def solve():
    """Index: 7029.
    Returns: the total number of marbles Hilton had in the end.
    """
    # L1
    initial_marbles = 26 # a box of 26 marbles
    found_marbles = 6 # found 6 marbles
    lost_marbles_initial = 10 # lost 10 marbles
    marbles_after_playing = initial_marbles + found_marbles - lost_marbles_initial

    # L2
    multiplier_lori = 2 # twice as many marbles
    lori_gave_marbles = multiplier_lori * lost_marbles_initial

    # L3
    total_marbles = marbles_after_playing + lori_gave_marbles

    # FA
    answer = total_marbles
    return answer