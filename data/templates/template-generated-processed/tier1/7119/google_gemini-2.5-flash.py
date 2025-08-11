def solve():
    """Index: 7119.
    Returns: the amount of money Jerry will have left after grocery shopping.
    """
    # L1
    mustard_oil_price_per_liter = 13 # $13 per liter
    mustard_oil_liters = 2 # 2 liters of mustard oil
    cost_mustard_oil = mustard_oil_price_per_liter * mustard_oil_liters

    # L2
    pasta_price_per_pound = 4 # $4 per pound
    pasta_pounds = 3 # 3 pounds of gluten-free penne pasta
    cost_pasta = pasta_price_per_pound * pasta_pounds

    # L3
    pasta_sauce_cost = 5 # 1 pound of pasta sauce that costs $5
    total_spent = cost_mustard_oil + cost_pasta + pasta_sauce_cost

    # L4
    initial_money = 50 # the rest of the $50
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer