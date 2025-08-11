def solve():
    """Index: 166.
    Returns: the maximum number of full-length movies Grandpa could have watched during these two days.
    """
    # L1
    hours_tuesday = 4 # 4 hours
    minutes_per_hour = 60 # WK
    extra_minutes_tuesday = 30 # 30 minutes
    total_minutes_tuesday = hours_tuesday * minutes_per_hour + extra_minutes_tuesday

    # L2
    minutes_per_movie = 90 # every movie lasts 90 minutes
    movies_tuesday = total_minutes_tuesday / minutes_per_movie

    # L3
    wednesday_multiplier = 2 # twice as many movies as he did on Tuesday
    movies_wednesday = wednesday_multiplier * movies_tuesday

    # L4
    total_movies = movies_tuesday + movies_wednesday

    # FA
    answer = total_movies
    return answer