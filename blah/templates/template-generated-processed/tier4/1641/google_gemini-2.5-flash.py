def solve():
    """Index: 1641.
    Returns: the number of times John uses the bathroom during the movie.
    """
    # L1
    movie_duration_hours = 2.5 # 2.5-hour movie
    minutes_per_hour = 60 # WK
    movie_duration_minutes = movie_duration_hours * minutes_per_hour

    # L2
    bathroom_frequency_minutes = 50 # every 50 minutes
    num_bathroom_uses = movie_duration_minutes / bathroom_frequency_minutes

    # FA
    answer = num_bathroom_uses
    return answer