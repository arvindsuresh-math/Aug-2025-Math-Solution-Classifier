def solve():
    """Index: 1061.
    Returns: the amount John paid.
    """
    # L1
    num_cakes = 3 # 3 cakes
    cost_per_cake = 12 # $12 each
    total_cost_cakes = num_cakes * cost_per_cake

    # L2
    num_people_splitting = 2 # splits the cost with his brother
    johns_payment = total_cost_cakes / num_people_splitting

    # FA
    answer = johns_payment
    return answer