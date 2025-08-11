def solve():
    """Index: 5382.
    Returns: the number of minutes left in the flight.
    """
    # L1
    num_episodes = 3 # 3 TV episodes
    episode_length_minutes = 25 # each 25 minutes long
    tv_watching_minutes = num_episodes * episode_length_minutes

    # L2
    sleep_duration_hours = 4.5 # 4 and a half hours
    minutes_per_hour = 60 # WK
    sleep_duration_minutes = sleep_duration_hours * minutes_per_hour

    # L3
    num_movies = 2 # 2 movies
    movie_length_hours = 1.75 # an hour and 45 minutes long (1 + 45/60 = 1.75 hours)
    movie_watching_minutes = num_movies * movie_length_hours * minutes_per_hour

    # L4
    total_activity_minutes = tv_watching_minutes + sleep_duration_minutes + movie_watching_minutes

    # L5
    flight_duration_hours = 10 # 10 hours long
    total_flight_minutes = flight_duration_hours * minutes_per_hour

    # L6
    remaining_flight_minutes = total_flight_minutes - total_activity_minutes

    # FA
    answer = remaining_flight_minutes
    return answer