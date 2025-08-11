def solve():
    """Index: 139.
    Returns: the total number of flights of stairs Janice walks (up and down) in a single day.
    """
    # L1
    flights_per_trip = 3 # 3 flights of stairs
    up_trips = 5 # goes up the three flights of stairs 5 times
    up_flights = flights_per_trip * up_trips

    # L2
    down_trips = 3 # down the three flights of stairs 3 times
    down_flights = flights_per_trip * down_trips

    # L3
    total_flights = up_flights + down_flights

    # FA
    answer = total_flights
    return answer