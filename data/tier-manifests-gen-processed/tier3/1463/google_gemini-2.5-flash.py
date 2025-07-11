def solve():
    """Index: 1463.
    Returns: the number of seconds Ned will have to diffuse the bomb.
    """
    # L1
    seconds_spent_running = 165 # Ned has spent 165 seconds running up the stairs
    time_per_flight = 11 # Ned can run up one flight of stairs in eleven seconds
    flights_climbed = seconds_spent_running / time_per_flight

    # L2
    total_flights = 20 # The building has twenty flights of stairs to the top floor
    remaining_flights = total_flights - flights_climbed

    # L3
    time_for_remaining_flights = remaining_flights * time_per_flight

    # L4
    initial_bomb_timer = 72 # The time bomb has 72 seconds left on the timer
    time_to_diffuse = initial_bomb_timer - time_for_remaining_flights

    # FA
    answer = time_to_diffuse
    return answer