def solve():
    """Index: 4626.
    Returns: the additional profit made by spending extra money to build the house.
    """
    # L1
    other_house_sale_price = 320000 # which sell at $320,000 each
    sale_price_multiplier = 1.5 # sells for 1.5 times as much
    this_house_sale_price = other_house_sale_price * sale_price_multiplier

    # L2
    worth_more_than_other_houses = this_house_sale_price - other_house_sale_price

    # L3
    extra_construction_cost = 100000 # is 100,000 more than the construction cost
    extra_profit = worth_more_than_other_houses - extra_construction_cost

    # FA
    answer = extra_profit
    return answer