def solve():
    """Index: 6838.
    Returns: the total duration John was on missions.
    """
    # L1
    initial_mission_duration = 5 # supposed to take 5 days
    longer_percentage = 0.6 # took 60% longer
    longer_duration = initial_mission_duration * longer_percentage

    # L2
    actual_first_mission_duration = initial_mission_duration + longer_duration

    # L3
    second_mission_duration = 3 # took 3 days
    total_mission_duration = actual_first_mission_duration + second_mission_duration

    # FA
    answer = total_mission_duration
    return answer