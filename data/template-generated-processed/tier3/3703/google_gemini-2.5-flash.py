def solve():
    """Index: 3703.
    Returns: the total time in seconds to get to the bottom of the garage from the top.
    """
    # L1
    total_floors = 12 # 12 floors
    floors_per_gate = 3 # Every 3rd floor has a gate
    num_gates = total_floors / floors_per_gate

    # L2
    time_per_gate_minutes = 2 # takes two minutes
    total_wait_time_minutes = num_gates * time_per_gate_minutes

    # L3
    seconds_per_minute = 60 # WK
    total_wait_time_seconds = total_wait_time_minutes * seconds_per_minute

    # L4
    distance_per_floor_feet = 800 # drive 800 feet
    speed_feet_per_second = 10 # at 10 feet/second
    time_per_floor_seconds = distance_per_floor_feet / speed_feet_per_second

    # L5
    total_driving_time_seconds = time_per_floor_seconds * total_floors

    # L6
    total_time_to_bottom_seconds = total_driving_time_seconds + total_wait_time_seconds

    # FA
    answer = total_time_to_bottom_seconds
    return answer