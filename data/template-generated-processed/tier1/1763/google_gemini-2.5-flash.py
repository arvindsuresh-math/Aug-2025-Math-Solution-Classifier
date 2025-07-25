def solve():
    """Index: 1763.
    Returns: the time left to get to the room without being late.
    """
    # L1
    time_to_gate = 15 # 15 minutes to arrive at the school gate
    time_gate_to_building = 6 # another 6 minutes to get to the school building
    total_time_to_building = time_to_gate + time_gate_to_building

    # L2
    total_allowed_time = 30 # thirty minutes to go to school
    time_left_to_room = total_allowed_time - total_time_to_building

    # FA
    answer = time_left_to_room
    return answer