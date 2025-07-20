def solve():
    """Index: 3249.
    Returns: the total cost for Briget's purchase.
    """
    # L1
    strawberry_cost_per_pound = 2.20 # A pound of strawberries costs $2.20
    strawberry_pounds = 5 # buy 5 pounds of strawberries
    total_strawberry_cost = strawberry_cost_per_pound * strawberry_pounds

    # L2
    cherry_cost_multiplier = 6 # cherries costs 6 times as much as strawberries
    cherry_cost_per_pound = strawberry_cost_per_pound * cherry_cost_multiplier

    # L3
    cherry_pounds = 5 # buy 5 pounds of cherries
    total_cherry_cost = cherry_cost_per_pound * cherry_pounds

    # L4
    total_cost = total_strawberry_cost + total_cherry_cost

    # FA
    answer = total_cost
    return answer