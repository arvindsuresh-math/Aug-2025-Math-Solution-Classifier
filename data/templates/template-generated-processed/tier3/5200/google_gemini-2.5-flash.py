def solve():
    """Index: 5200.
    Returns: the cost of each pair of pants.
    """
    # L1
    cost_per_tshirt = 100 # a t-shirt costs $100
    num_tshirts = 5 # 5 t-shirts
    total_cost_tshirts = cost_per_tshirt * num_tshirts

    # L2
    total_bill = 1500 # for $1500
    total_cost_pants = total_bill - total_cost_tshirts

    # L3
    num_pants = 4 # 4 pairs of pants
    cost_per_pair_of_pants = total_cost_pants / num_pants

    # FA
    answer = cost_per_pair_of_pants
    return answer