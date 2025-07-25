def solve():
    """Index: 166.
    Returns: the maximum number of full-length movies Grandpa could have watched during these two days.
    """
    # L1
    hours_tuesday = 4 # 4 hours and 30 minutes
    minutes_tuesday = 30 # 4 hours and 30 minutes
    minutes_per_hour = 60 # WK
    total_minutes_tuesday = hours_tuesday * minutes_per_hour + minutes_tuesday

    # L2
    movie_duration_minutes = 90 # every movie lasts 90 minutes
    movies_tuesday = total_minutes_tuesday / movie_duration_minutes

    # L3
    wednesday_multiplier = 2 # twice as many movies
    movies_wednesday = wednesday_multiplier * movies_tuesday

    # L4
    total_movies = movies_tuesday + movies_wednesday

    # FA
    answer = total_movies
    return answer