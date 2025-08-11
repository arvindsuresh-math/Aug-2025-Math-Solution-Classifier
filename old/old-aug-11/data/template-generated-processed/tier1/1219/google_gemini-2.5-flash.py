def solve():
    """Index: 1219.
    Returns: the total number of pieces of chicken needed for all orders.
    """
    # L1
    num_fried_dinner_orders = 2 # 2 Fried Chicken Dinner orders
    chicken_per_fried_dinner = 8 # uses 8 pieces of chicken
    chicken_for_fried_dinners = num_fried_dinner_orders * chicken_per_fried_dinner

    # L2
    num_pasta_orders = 6 # 6 Chicken Pasta orders
    chicken_per_pasta_order = 2 # uses 2 pieces of chicken
    chicken_for_pasta = num_pasta_orders * chicken_per_pasta_order

    # L3
    num_bbq_orders = 3 # 3 Barbecue Chicken orders
    chicken_per_bbq_order = 3 # uses 3 pieces of chicken
    chicken_for_bbq = num_bbq_orders * chicken_per_bbq_order

    # L4
    total_chicken_needed = chicken_for_fried_dinners + chicken_for_pasta + chicken_for_bbq

    # FA
    answer = total_chicken_needed
    return answer