def solve():
    """Index: 369.
    Returns: the total money Monika spent throughout her day.
    """
    # L1
    movie_cost_per_movie = 24 # each cost $24
    num_movies = 3 # watched 3 movies
    movie_total_cost = movie_cost_per_movie * num_movies

    # L2
    num_bags_beans = 20 # 20 bags of beans
    cost_per_bag_beans = 1.25 # $1.25/bag
    farmers_market_total_cost = num_bags_beans * cost_per_bag_beans

    # L3
    mall_cost = 250 # spent $250
    total_spent = mall_cost + movie_total_cost + farmers_market_total_cost

    # FA
    answer = total_spent
    return answer