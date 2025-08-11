def solve():
    """Index: 167.
    Returns: the total amount of money required to film Janet's entire newest film.
    """
    # L1
    previous_movie_hours = 2 # previous 2-hour long movie
    minutes_per_hour = 60 # WK
    previous_movie_minutes = previous_movie_hours * minutes_per_hour

    # L2
    percent_longer = 0.6 # 60% longer
    extra_minutes = previous_movie_minutes * percent_longer

    # L3
    newest_movie_minutes = previous_movie_minutes + extra_minutes

    # L4
    previous_cost_per_minute = 50 # $50 per minute to film
    cost_multiplier = 2 # twice as much per minute
    newest_cost_per_minute = previous_cost_per_minute * cost_multiplier

    # L5
    total_cost = newest_movie_minutes * newest_cost_per_minute

    # FA
    answer = total_cost
    return answer