def solve():
    """Index: 6785.
    Returns: the total money Hannah spent.
    """
    # L1
    num_sweatshirts = 3 # 3 sweatshirts
    cost_per_sweatshirt = 15 # Each sweatshirt cost 15$
    cost_sweatshirts = num_sweatshirts * cost_per_sweatshirt

    # L2
    num_tshirts = 2 # 2 T-shirts
    cost_per_tshirt = 10 # each t-shirt cost 10$
    cost_tshirts = num_tshirts * cost_per_tshirt

    # L3
    total_spent = cost_sweatshirts + cost_tshirts

    # FA
    answer = total_spent
    return answer