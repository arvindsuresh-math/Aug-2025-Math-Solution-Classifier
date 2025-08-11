def solve():
    """Index: 6048.
    Returns: the total amount Athena spent on snacks.
    """
    # L1
    num_sandwiches = 3 # 3 sandwiches
    price_per_sandwich = 3 # $3 each
    cost_sandwiches = num_sandwiches * price_per_sandwich

    # L2
    num_fruit_drinks = 2 # 2 fruit drinks
    price_per_fruit_drink = 2.5 # $2.5 each
    cost_fruit_drinks = num_fruit_drinks * price_per_fruit_drink

    # L3
    total_spent = cost_sandwiches + cost_fruit_drinks

    # FA
    answer = total_spent
    return answer