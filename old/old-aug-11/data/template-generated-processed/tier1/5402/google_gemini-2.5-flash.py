def solve():
    """Index: 5402.
    Returns: the total time to travel from New York to Miami.
    """
    # L1
    flight_time_nyc_chicago = 4 # flies for 4 hours from New York City to Chicago
    layover_time_chicago = 1 # stays at the port in Chicago for 1 hour
    time_before_miami_departure = flight_time_nyc_chicago + layover_time_chicago

    # L2
    miami_flight_multiplier = 3 # three times as many hours to fly to Miami
    flight_time_chicago_miami = miami_flight_multiplier * flight_time_nyc_chicago

    # L3
    total_travel_time = flight_time_chicago_miami + time_before_miami_departure

    # FA
    answer = total_travel_time
    return answer