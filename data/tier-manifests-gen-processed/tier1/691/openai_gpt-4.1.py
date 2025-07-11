def solve():
    """Index: 691.
    Returns: the number of hours Chance's flight took from New York to Cape Town.
    """
    # L1
    departure_time_ny = 6 # 6:00 a.m. ET on Monday
    flight_duration_london_ny = 18 # arrived in New York 18 hours later
    arrival_time_ny = (departure_time_ny + flight_duration_london_ny) % 24

    # L2
    arrival_time_cape_town = 10 # arrived in Cape town at 10:00 a.m ET on Tuesday
    flight_duration_ny_cape_town = (arrival_time_cape_town - arrival_time_ny) % 24

    # FA
    answer = flight_duration_ny_cape_town
    return answer