def solve(
        num_turns_required: int = 4, # total of 4 right-hand turns
        distance_after_first_turn: int = 5, # After the 1st turn, it travels 5 meters
        distance_after_second_turn: int = 8, # After the 2nd turn, it travels 8 meters
        distance_after_fourth_turn: int = 0, # at the 4th turn, it immediately exits the tunnel
        total_distance_driven: int = 23 # If the car has driven a total of 23 meters around the ring
    ):
    """Index: 32.
    Returns: the distance the car traveled after the 3rd turn.
    """
    #: L1
    known_distances_sum = distance_after_first_turn + distance_after_second_turn + distance_after_fourth_turn

    #: L2
    distance_after_third_turn = total_distance_driven - known_distances_sum

    answer = distance_after_third_turn # FINAL ANSWER
    return answer