def solve():
    """Index: 6883.
    Returns: the total cost to replace the movies.
    """
    # L1
    dvd_cost = 10 # DVDs for $10 each
    vhs_trade_in_value = 2 # trade in his VHS for $2 each
    cost_per_movie = dvd_cost - vhs_trade_in_value

    # L2
    num_movies = 100 # 100 movies
    total_cost = cost_per_movie * num_movies

    # FA
    answer = total_cost
    return answer