def solve():
    """Index: 32.
    Returns: the distance the car traveled after the 3rd turn.
    """
    # L1
    after_1st_turn = 5 # travels 5 meters after the 1st turn
    after_2nd_turn = 8 # travels 8 meters after the 2nd turn
    after_4th_turn = 0 # immediately exits the tunnel after the 4th turn
    sum_known_distances = after_1st_turn + after_2nd_turn + after_4th_turn

    # L2
    total_distance = 23 # driven a total of 23 meters around the ring
    after_3rd_turn = total_distance - sum_known_distances

    # FA
    answer = after_3rd_turn
    return answer