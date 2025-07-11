def solve():
    """Index: 167.
    Returns: the total amount of money required to film Janet's entire newest film.
    """
    # L1
    previous_movie_duration_hours = 2 # previous 2-hour long movie
    minutes_per_hour = 60 # WK
    previous_movie_duration_minutes = previous_movie_duration_hours * minutes_per_hour

    # L2
    longer_percent = 0.6 # 60% longer
    new_movie_longer_minutes = previous_movie_duration_minutes * longer_percent

    # L3
    new_movie_total_duration_minutes = previous_movie_duration_minutes + new_movie_longer_minutes

    # L4
    previous_movie_cost_per_minute = 50 # cost $50 per minute to film
    cost_multiplier = 2 # twice as much per minute
    new_movie_cost_per_minute = previous_movie_cost_per_minute * cost_multiplier

    # L5
    total_cost_new_movie = new_movie_total_duration_minutes * new_movie_cost_per_minute

    # FA
    answer = total_cost_new_movie
    return answer