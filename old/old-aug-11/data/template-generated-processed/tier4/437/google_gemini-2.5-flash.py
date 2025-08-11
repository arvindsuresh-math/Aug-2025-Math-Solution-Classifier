def solve():
    """Index: 437.
    Returns: the number of chickens Lao sold.
    """
    # L1
    bag_feed_weight = 20 # weighs 20 pounds
    feed_per_chicken = 2 # Each chicken will need 2 pounds of feed
    chickens_per_bag = bag_feed_weight / feed_per_chicken

    # L2
    bag_cost = 2 # costs $2
    cost_per_chicken = bag_cost / chickens_per_bag

    # L3
    sell_price_per_chicken = 1.50 # sell each chicken for $1.50
    profit_per_chicken = sell_price_per_chicken - cost_per_chicken

    # L4
    total_profit = 65 # makes $65 profit
    num_chickens_sold = total_profit / profit_per_chicken

    # FA
    answer = num_chickens_sold
    return answer