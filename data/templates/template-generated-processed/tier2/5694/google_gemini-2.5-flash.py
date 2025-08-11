def solve():
    """Index: 5694.
    Returns: the total duration of the movie marathon.
    """
    # L1
    first_movie_duration = 2 # The first movie is 2 hours long
    longer_percentage = 0.5 # The next movie is 50% longer
    second_movie_extra_duration = first_movie_duration * longer_percentage

    # L2
    second_movie_duration = first_movie_duration + second_movie_extra_duration

    # L3
    combined_first_two_movies_duration = second_movie_duration + first_movie_duration

    # L4
    shorter_amount = 1 # 1 hour shorter
    last_movie_duration = combined_first_two_movies_duration - shorter_amount

    # L5
    total_marathon_duration = combined_first_two_movies_duration + last_movie_duration

    # FA
    answer = total_marathon_duration
    return answer