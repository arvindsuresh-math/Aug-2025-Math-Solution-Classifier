def solve():
    """Index: 2470.
    Returns: the number of points Brenda is ahead after both plays.
    """
    # L1
    brenda_initial_ahead = 22 # Brenda is ahead by 22 points
    brenda_play = 15 # she makes a 15-point play
    brenda_after_play = brenda_initial_ahead + brenda_play

    # L2
    david_play = 32 # David responds with a 32-point play
    brenda_final_ahead = brenda_after_play - david_play

    # FA
    answer = brenda_final_ahead
    return answer