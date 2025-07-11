def solve():
    """Index: 942.
    Returns: the number of miles Paul runs while watching movies.
    """
    # L1
    num_movies = 2 # He watches two movies
    avg_movie_length_hours = 1.5 # average length of 1.5 hours
    total_hours = num_movies * avg_movie_length_hours

    # L2
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # L3
    minutes_per_mile = 12 # He can run a mile in 12 minutes
    miles_run = total_minutes / minutes_per_mile

    # FA
    answer = miles_run
    return answer