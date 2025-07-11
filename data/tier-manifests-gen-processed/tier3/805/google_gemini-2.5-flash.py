def solve():
    """Index: 805.
    Returns: the total number of movies shown throughout the day.
    """
    # L1
    open_hours = 8 # movie theater is open for 8 hours
    movie_duration = 2 # each movie lasts 2 hours
    movies_per_screen_per_day = open_hours / movie_duration

    # L2
    num_screens = 6 # 6 screens
    total_movies = num_screens * movies_per_screen_per_day

    # FA
    answer = total_movies
    return answer