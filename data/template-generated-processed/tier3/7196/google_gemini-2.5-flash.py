def solve():
    """Index: 7196.
    Returns: the number of hours Aren has left for a nap.
    """
    # L1
    minutes_per_hour = 60 # WK
    flight_hours = 11 # 11 hours 20 minutes
    flight_minutes_extra = 20 # 11 hours 20 minutes
    total_flight_minutes = minutes_per_hour * flight_hours + flight_minutes_extra

    # L2
    reading_hours = 2 # 2 hours reading
    movie_hours = 4 # 4 hours watching two movies
    dinner_minutes = 30 # 30 minutes eating his dinner
    radio_minutes = 40 # 40 minutes listening to the radio
    game_hours = 1 # 1 hour 10 minutes playing games
    game_minutes_extra = 10 # 1 hour 10 minutes playing games
    reading_minutes = reading_hours * minutes_per_hour
    movie_minutes = movie_hours * minutes_per_hour
    game_minutes = game_hours * minutes_per_hour + game_minutes_extra
    total_activity_minutes = reading_minutes + movie_minutes + dinner_minutes + radio_minutes + game_minutes

    # L3
    nap_minutes = total_flight_minutes - total_activity_minutes

    # L4
    nap_hours = nap_minutes / minutes_per_hour

    # FA
    answer = nap_hours
    return answer