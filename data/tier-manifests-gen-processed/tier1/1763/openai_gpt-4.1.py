def solve():
    """Index: 1763.
    Returns: the number of minutes left to get to the room without being late.
    """
    # L1
    time_to_gate = 15 # it takes us 15 minutes to arrive at the school gate
    time_to_building = 6 # and another 6 minutes to get to the school building
    total_time_spent = time_to_gate + time_to_building

    # L2
    total_time_allowed = 30 # have thirty minutes to go to school
    time_left = total_time_allowed - total_time_spent

    # FA
    answer = time_left
    return answer