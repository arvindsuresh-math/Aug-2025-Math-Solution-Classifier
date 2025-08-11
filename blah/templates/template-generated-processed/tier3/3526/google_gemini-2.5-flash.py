def solve():
    """Index: 3526.
    Returns: the total cost in cents for buying the cheaper fruit.
    """
    # L1
    total_cost_apples_cents = 200 # 10 apples for $2
    num_apples = 10 # 10 apples
    price_per_apple_cents = total_cost_apples_cents / num_apples

    # L2
    total_cost_oranges_cents = 150 # 5 oranges for $1.50
    num_oranges = 5 # 5 oranges
    price_per_orange_cents = total_cost_oranges_cents / num_oranges

    # L4
    quantity_to_buy = 12 # 12 of the cheaper of the two fruits
    total_cost_cheaper_fruit_cents = price_per_apple_cents * quantity_to_buy

    # FA
    answer = total_cost_cheaper_fruit_cents
    return answer