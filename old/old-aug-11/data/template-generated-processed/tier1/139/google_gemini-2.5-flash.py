def solve():
    """Index: 139.
    Returns: the total number of flights of stairs Janice walks in a single day.
    """
    # L1
    flights_per_trip = 3 # 3 flights of stairs
    times_up = 5 # up the three flights of stairs 5 times
    total_flights_up = flights_per_trip * times_up

    # L2
    times_down = 3 # down the the three flights of stairs 3 times
    total_flights_down = flights_per_trip * times_down

    # L3
    total_flights_walked = total_flights_up + total_flights_down

    # FA
    answer = total_flights_walked
    return answer