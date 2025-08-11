def solve():
    """Index: 2160.
    Returns: the total cost of John's outfit.
    """
    # L1
    pants_cost = 50 # His pants cost $50
    shirt_percent_more = 0.6 # shirt cost 60% more
    shirt_extra_cost = pants_cost * shirt_percent_more

    # L2
    shirt_cost = pants_cost + shirt_extra_cost

    # L3
    total_cost = shirt_cost + pants_cost

    # FA
    answer = total_cost
    return answer