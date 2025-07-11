def solve():
    """Index: 1837.
    Returns: the total time in minutes from the first station to Mr. Langsley's workplace.
    """
    # L1
    arrival_hour = 9 # arrives at work at 9:00 a.m.
    pickup_hour = 6 # picks him up at 6:00 a.m.
    total_hours = arrival_hour - pickup_hour

    # L2
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # L3
    minutes_to_first_station = 40 # takes forty minutes to arrive at the first station
    time_from_first_station = total_minutes - minutes_to_first_station

    # FA
    answer = time_from_first_station
    return answer