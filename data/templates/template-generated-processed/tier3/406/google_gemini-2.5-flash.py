def solve():
    """Index: 406.
    Returns: the total time in hours spent cooking and watching movies.
    """
    # L1
    first_movie_hours = 1 # The first movie is 1 hour and 30 minutes long
    first_movie_extra_minutes = 30 # The first movie is 1 hour and 30 minutes long
    minutes_per_hour = 60 # WK
    first_movie_minutes_from_hours = first_movie_hours * minutes_per_hour
    first_movie_total_minutes = first_movie_minutes_from_hours + first_movie_extra_minutes

    # L2
    second_movie_extra_minutes = 30 # the second movie is 30 minutes longer than the first
    second_movie_total_minutes = first_movie_total_minutes + second_movie_extra_minutes

    # L3
    total_movie_watching_minutes = first_movie_total_minutes + second_movie_total_minutes

    # L4
    popcorn_making_minutes = 10 # spent 10 minutes making popcorn
    fries_multiplier = 2 # twice as long making fries
    fries_cooking_minutes = popcorn_making_minutes * fries_multiplier

    # L5
    total_cooking_minutes = popcorn_making_minutes + fries_cooking_minutes

    # L6
    total_time_in_minutes = total_movie_watching_minutes + total_cooking_minutes

    # L7
    total_time_in_hours = total_time_in_minutes / minutes_per_hour

    # FA
    answer = total_time_in_hours
    return answer