def solve():
    """Index: 437.
    Returns: the number of chickens Lao sold.
    """
    # L1
    feed_bag_weight = 20 # A bag of chicken feed weighs 20 pounds
    feed_per_chicken = 2 # Each chicken will need 2 pounds of feed
    chickens_per_bag = feed_bag_weight / feed_per_chicken

    # L2
    feed_bag_cost = 2 # A bag of chicken feed costs $2
    cost_per_chicken = feed_per_chicken / chickens_per_bag

    # L3
    sale_price_per_chicken = 1.5 # He can sell each chicken for $1.50
    profit_per_chicken = sale_price_per_chicken - cost_per_chicken

    # L4
    total_profit = 65 # He makes $65 profit from selling chickens
    num_chickens_sold = total_profit / profit_per_chicken

    # FA
    answer = num_chickens_sold
    return answer