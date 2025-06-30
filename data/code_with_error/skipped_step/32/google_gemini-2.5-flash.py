def solve(
        num_turns: int = 4, # a total of 4 right-hand turns
        dist_after_1st_turn: int = 5, # After the 1st turn, it travels 5 meters
        dist_after_2nd_turn: int = 8, # After the 2nd turn, it travels 8 meters
        total_dist_around_ring: int = 23 # driven a total of 23 meters around the ring
    ):
    """Index: 32.
    Returns: the distance the car traveled after the 3rd turn.
    """

    #: L1

    #: L2
    distance_after_3rd_turn = total_dist_around_ring - dist_after_2nd_turn

    #: FA
    answer = distance_after_3rd_turn
    return answer