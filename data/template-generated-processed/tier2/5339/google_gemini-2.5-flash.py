def solve():
    """Index: 5339.
    Returns: the lowest price the woman can pay for 16 oz of butter.
    """
    # L1
    normal_price_4oz_package = 2.0 # normally sell for $2.0 each
    discount_percent_decimal = 0.5 # a 50% discount
    cost_per_discounted_4oz_package = normal_price_4oz_package * discount_percent_decimal

    # L2
    cost_8oz_package = 4 # an 8oz package of store butter for $4
    num_4oz_packages_needed = 2 # two 4 oz packages
    total_cost_option2 = cost_8oz_package + num_4oz_packages_needed * cost_per_discounted_4oz_package

    # L3
    cost_16oz_package = 7 # a single 16 oz package of the store-brand butter for $7
    lowest_price = min(total_cost_option2, cost_16oz_package)

    # FA
    answer = lowest_price
    return answer