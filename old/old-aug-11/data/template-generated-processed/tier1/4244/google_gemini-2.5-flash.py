def solve():
    """Index: 4244.
    Returns: the difference in chickens John took compared to Ray.
    """
    # L1
    ray_took = 10 # If Ray took 10 chickens
    mary_took_more_than_ray = 6 # Ray took 6 chickens less than Mary
    mary_took = ray_took + mary_took_more_than_ray

    # L2
    john_took_more_than_mary = 5 # John took 5 more of the chickens than Mary took
    john_took = mary_took + john_took_more_than_mary

    # L3
    john_more_than_ray = john_took - ray_took

    # FA
    answer = john_more_than_ray
    return answer