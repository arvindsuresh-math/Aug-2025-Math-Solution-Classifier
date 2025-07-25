def solve():
    """Index: 2238.
    Returns: the number of chickens Paul was left with to sell at the market.
    """
    # L1
    sold_to_neighbor = 12 # sold his neighbor 12 chickens
    sold_to_customer = 25 # sold another 25 chickens
    total_sold_before_market = sold_to_neighbor + sold_to_customer

    # L2
    initial_chickens = 80 # 80 chickens in total
    chickens_left = initial_chickens - total_sold_before_market

    # FA
    answer = chickens_left
    return answer