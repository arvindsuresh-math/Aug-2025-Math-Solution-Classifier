def solve():
    """Index: 6743.
    Returns: the total profit made from selling the cattle.
    """
    # L1
    feed_cost_multiplier = 0.2 # It cost 20% more than that to feed them
    initial_cattle_cost = 40000 # buys 100 head of cattle for $40,000
    additional_feed_cost = feed_cost_multiplier * initial_cattle_cost

    # L2
    total_feed_cost = initial_cattle_cost + additional_feed_cost

    # L3
    total_expenses = total_feed_cost + initial_cattle_cost

    # L4
    sell_price_per_pound = 2 # sell for $2 per pound
    cow_weight_pounds = 1000 # each weigh 1000 pounds
    price_per_cow = sell_price_per_pound * cow_weight_pounds

    # L5
    num_cattle = 100 # buys 100 head of cattle
    total_revenue = price_per_cow * num_cattle

    # L6
    profit = total_revenue - total_expenses

    # FA
    answer = profit
    return answer