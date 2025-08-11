def solve():
    """Index: 659.
    Returns: Elizabeth's net profit from selling granola bags.
    """
    # L1
    ingredient_cost_per_bag = 3.00 # $3.00 worth of ingredients to make a bag
    total_bags = 20 # she makes 20 bags
    total_ingredient_cost = ingredient_cost_per_bag * total_bags

    # L2
    full_price_bags = 15 # sold 15 bags
    full_price = 6.00 # sells them for $6.00 a bag
    full_price_revenue = full_price_bags * full_price

    # L3
    discount_bags = 5 # remaining 5 bags
    discount_price = 4.00 # marks down to $4.00
    discount_revenue = discount_bags * discount_price

    # L4
    total_revenue = full_price_revenue + discount_revenue

    # L5
    net_profit = total_revenue - total_ingredient_cost

    # FA
    answer = net_profit
    return answer