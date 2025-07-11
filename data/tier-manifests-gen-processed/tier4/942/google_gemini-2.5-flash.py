def solve():
    """Index: 942.
    Returns: the total number of miles Paul runs.
    """
    # L1
    num_movies = 2 # two movies
    avg_movie_length_hours = 1.5 # average length of 1.5 hours
    total_running_hours = num_movies * avg_movie_length_hours

    # L2
    minutes_per_hour = 60 # WK
    total_running_minutes = total_running_hours * minutes_per_hour

    # L3
    minutes_per_mile = 12 # run a mile in 12 minutes
    total_miles_run = total_running_minutes / minutes_per_mile

    # FA
    answer = total_miles_run
    return answer