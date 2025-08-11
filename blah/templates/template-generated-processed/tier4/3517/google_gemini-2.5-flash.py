def solve():
    """Index: 3517.
    Returns: the cost of each serving of nuts in cents.
    """
    # L1
    bag_cost_dollars = 25.00 # $25.00 a bag
    coupon_value_dollars = 5.00 # $5.00 coupon
    sale_cost_dollars = bag_cost_dollars - coupon_value_dollars

    # L2
    serving_size_oz = 1 # 1 oz of mixed nuts
    bag_size_oz = 40 # holds 40 oz of mixed nuts
    num_servings = bag_size_oz / serving_size_oz

    # L3
    cost_per_serving_dollars = sale_cost_dollars / num_servings

    # Convert to cents as required by the question
    cents_per_dollar = 100 # WK
    cost_per_serving_cents = cost_per_serving_dollars * cents_per_dollar

    # FA
    answer = cost_per_serving_cents
    return answer