def solve(
    distance_after_1st_turn: int = 5,  # After the 1st turn, it travels 5 meters
    distance_after_2nd_turn: int = 8,  # After the 2nd turn, it travels 8 meters
    distance_after_4th_turn: int = 0,  # At the 4th turn, it immediately exits (0 meters)
    total_distance: int = 23  # The car has driven a total of 23 meters around the ring
):
    """Index: 32.
    Returns: the distance traveled after the 3rd turn.
    """

    #: L1
    distance_known = distance_after_1st_turn + distance_after_2nd_turn + distance_after_4th_turn

    #: L2
    distance_after_3rd_turn = total_distance - distance_known

    answer = distance_after_3rd_turn  # FINAL ANSWER
    return answer