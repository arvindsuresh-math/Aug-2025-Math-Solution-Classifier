def solve():
    """Index: 7306.
    Returns: the amount of change Roxanne must get.
    """
    # L1
    num_lemonade_cups = 2 # 2 cups of lemonade
    price_per_lemonade = 2 # $2 each
    cost_lemonade = price_per_lemonade * num_lemonade_cups

    # L2
    price_per_sandwich = 2.50 # $2.50 each
    num_sandwiches = 2 # 2 sandwiches
    cost_sandwiches = price_per_sandwich * num_sandwiches

    # L3
    total_cost = cost_lemonade + cost_sandwiches

    # L4
    bill_amount = 20 # $20 bill
    change_amount = bill_amount - total_cost

    # FA
    answer = change_amount
    return answer