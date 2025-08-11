def solve():
    """Index: 1465.
    Returns: the number of feet Jack is further down than when he started.
    """
    # L1
    steps_per_flight = 12 # 12 steps
    inches_per_step = 8 # 8 inches high
    inches_per_flight = steps_per_flight * inches_per_step

    # L2
    flights_down = 6 # down six flights of stairs
    flights_up = 3 # up three flights of stairs
    net_flights_down = flights_down - flights_up

    # L3
    total_inches_down = inches_per_flight * net_flights_down

    # L4
    inches_per_foot = 12 # WK
    total_feet_down = total_inches_down / inches_per_foot

    # FA
    answer = total_feet_down
    return answer