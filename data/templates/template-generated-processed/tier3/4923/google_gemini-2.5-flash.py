def solve():
    """Index: 4923.
    Returns: the number of seconds later Jake will get to the ground floor.
    """
    # L1
    num_floors = 9 # 9th floor
    steps_per_floor = 30 # 30 steps across each floor
    total_steps_jake = num_floors * steps_per_floor

    # L2
    jake_descent_rate = 3 # descending 3 steps every second
    jake_time_seconds = total_steps_jake / jake_descent_rate

    # L3
    elevator_time_seconds = 60 # take a minute to get to ground level
    time_difference = jake_time_seconds - elevator_time_seconds

    # FA
    answer = time_difference
    return answer