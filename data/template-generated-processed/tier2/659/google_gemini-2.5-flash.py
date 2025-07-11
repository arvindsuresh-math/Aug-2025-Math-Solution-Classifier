def solve():
    """Index: 659.
    Returns: Elizabeth's net profit.
    """
    # L1
    cost_per_bag_ingredients = 3.00 # $3.00 worth of ingredients
    bags_made = 20 # makes 20 bags
    total_ingredient_cost = cost_per_bag_ingredients * bags_made

    # L2
    bags_sold_initial = 15 # sold 15 bags
    price_initial = 6.00 # sells them for $6.00 a bag
    revenue_initial_sales = bags_sold_initial * price_initial

    # L3
    bags_sold_discounted = 5 # remaining 5 bags
    price_discounted = 4.00 # marks the remaining 5 bags down to $4.00
    revenue_discounted_sales = bags_sold_discounted * price_discounted

    # L4
    total_revenue = revenue_initial_sales + revenue_discounted_sales

    # L5
    net_profit = total_revenue - total_ingredient_cost

    # FA
    answer = net_profit
    return answer