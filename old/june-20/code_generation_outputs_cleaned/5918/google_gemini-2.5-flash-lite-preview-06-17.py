def solve(
    rate_rise: int = 50, # rise at a rate of 50 feet per minute
    rate_descend: int = 10, # descend at a rate of 10 feet per minute
    time_pulling_chain_1: int = 15, # pulled the chain for 15 minutes
    time_releasing_rope: int = 10, # released the rope for 10 minutes
    time_pulling_chain_2: int = 15 # pulled the chain for another 15 minutes
):
    """Index: 5918.
    Returns: the highest elevation reached by the balloon.
    """
    #: L1
    elevation_gain_1 = rate_rise * time_pulling_chain_1

    #: L2
    elevation_loss = rate_descend * time_releasing_rope

    #: L3
    elevation_gain_2 = rate_rise * time_pulling_chain_2

    #: L4
    highest_elevation = elevation_gain_1 - elevation_loss + elevation_gain_2

    answer = highest_elevation # FINAL ANSWER
    return answer