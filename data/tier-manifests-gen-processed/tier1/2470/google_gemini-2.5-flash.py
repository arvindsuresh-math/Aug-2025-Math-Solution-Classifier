def solve():
    """Index: 2470.
    Returns: the number of points Brenda is ahead by.
    """
    # L1
    brenda_initial_lead = 22 # ahead by 22 points
    brenda_play_points = 15 # makes a 15-point play
    brenda_lead_after_her_play = brenda_initial_lead + brenda_play_points

    # L2
    david_play_points = 32 # responds with a 32-point play
    brenda_final_lead = brenda_lead_after_her_play - david_play_points

    # FA
    answer = brenda_final_lead
    return answer