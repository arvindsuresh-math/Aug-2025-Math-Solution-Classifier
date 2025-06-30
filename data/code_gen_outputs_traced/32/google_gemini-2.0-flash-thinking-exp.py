def solve(
    total_turns: int = 4, # requires a total of 4 right-hand turns
    distance_after_1st_turn: int = 5, # After the 1st turn, it travels 5 meters
    distance_after_2nd_turn: int = 8, # After the 2nd turn, it travels 8 meters
    distance_after_4th_turn: int = 0, # at the 4th turn, it immediately exits the tunnel (implies 0 distance after)
    total_distance_around_ring: int = 23 # If the car has driven a total of 23 meters around the ring
):
    """Index: 32.
    Returns: the distance the car traveled after the 3rd turn.
    """

    #: L1
    distance_after_turns_1_2_4 = distance_after_1st_turn + distance_after_2nd_turn + distance_after_4th_turn # eval: 13 = 5 + 8 + 0

    #: L2
    distance_after_3rd_turn = total_distance_around_ring - distance_after_turns_1_2_4 # eval: 10 = 23 - 13

    #: FA
    answer = distance_after_3rd_turn # eval: 10 = 10
    return answer # eval: return 10
