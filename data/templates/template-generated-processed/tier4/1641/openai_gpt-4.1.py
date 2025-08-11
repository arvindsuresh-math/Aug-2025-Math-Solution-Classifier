def solve():
    """Index: 1641.
    Returns: the number of times John uses the bathroom during the movie.
    """
    # L1
    movie_hours = 2.5 # 2.5-hour movie
    minutes_per_hour = 60 # WK
    movie_minutes = movie_hours * minutes_per_hour

    # L2
    bathroom_interval = 50 # every 50 minutes
    bathroom_uses = movie_minutes / bathroom_interval

    # FA
    answer = bathroom_uses
    return answer