def solve(
    total_distance: int = 23,  # the car has driven a total of 23 meters around the ring
    first_turn_distance: int = 5,  # after the 1st turn, it travels 5 meters
    second_turn_distance: int = 8,  # after the 2nd turn, it travels 8 meters
    fourth_turn_distance: int = 0  # at the 4th turn, it immediately exits the tunnel
):
    """Index: 32.
    Returns: the distance traveled after the 3rd turn.
    """

    #: L1
    known_distances = first_turn_distance + second_turn_distance + fourth_turn_distance

    #: L2
    third_turn_distance = total_distance - known_distances

    #: FA
    answer = third_turn_distance
    return answer