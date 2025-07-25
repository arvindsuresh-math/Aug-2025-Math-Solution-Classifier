def solve():
    """Index: 1837.
    Returns: the total time taken in minutes from the first station to Mr. Langsley's workplace.
    """
    # L1
    end_hour = 9 # arrives at work at 9:00 a.m.
    start_hour = 6 # picks him up at 6:00 a.m.
    total_journey_hours = end_hour - start_hour

    # L2
    minutes_per_hour = 60 # WK
    total_journey_minutes = total_journey_hours * minutes_per_hour

    # L3
    time_to_first_station = 40 # takes forty minutes to arrive at the first station
    time_from_first_station_to_work = total_journey_minutes - time_to_first_station

    # FA
    answer = time_from_first_station_to_work
    return answer