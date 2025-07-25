def solve():
    """Index: 369.
    Returns: the total amount of money Monika spent throughout her day.
    """
    # L1
    movie_cost_per = 24 # each cost $24
    num_movies = 3 # watched 3 movies
    movie_total = movie_cost_per * num_movies

    # L2
    num_bags = 20 # 20 bags of beans
    cost_per_bag = 1.25 # $1.25/bag
    beans_total = num_bags * cost_per_bag

    # L3
    mall_spent = 250 # spent $250 at the mall
    total_spent = mall_spent + movie_total + beans_total

    # FA
    answer = total_spent
    return answer