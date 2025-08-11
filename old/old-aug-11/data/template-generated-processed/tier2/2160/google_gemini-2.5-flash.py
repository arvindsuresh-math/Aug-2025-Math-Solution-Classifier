def solve():
    """Index: 2160.
    Returns: the total cost of John's outfit.
    """
    # L1
    pants_cost = 50 # His pants cost $50
    shirt_cost_percentage_more = 0.6 # 60% more
    cost_more_than_pants = pants_cost * shirt_cost_percentage_more

    # L2
    shirt_cost = pants_cost + cost_more_than_pants

    # L3
    total_outfit_cost = shirt_cost + pants_cost

    # FA
    answer = total_outfit_cost
    return answer