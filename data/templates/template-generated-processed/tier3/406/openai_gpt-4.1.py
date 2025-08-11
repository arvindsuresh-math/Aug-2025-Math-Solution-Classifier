def solve():
    """Index: 406.
    Returns: the total time in hours Joseph and his friends spent cooking and watching the movies.
    """
    # L1
    hour_in_minutes = 60 # an hour has 60 minutes
    first_movie_extra_minutes = 30 # first movie is 1 hour and 30 minutes
    first_movie_minutes = hour_in_minutes + first_movie_extra_minutes

    # L2
    second_movie_extra_minutes = 30 # second movie is 30 minutes longer than the first
    second_movie_minutes = first_movie_minutes + second_movie_extra_minutes

    # L3
    total_movie_minutes = first_movie_minutes + second_movie_minutes

    # L4
    popcorn_minutes = 10 # 10 minutes making popcorn
    fries_multiplier = 2 # twice as long making fries
    fries_minutes = popcorn_minutes * fries_multiplier

    # L5
    total_cooking_minutes = popcorn_minutes + fries_minutes

    # L6
    total_minutes = total_movie_minutes + total_cooking_minutes

    # L7
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer