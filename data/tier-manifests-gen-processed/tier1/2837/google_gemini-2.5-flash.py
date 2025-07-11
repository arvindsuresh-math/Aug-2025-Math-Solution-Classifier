def solve():
    """Index: 2837.
    Returns: the total amount Leila should pay Ali.
    """
    # L1
    price_chocolate_cake = 12 # $12 each
    num_chocolate_cakes = 3 # 3 chocolate cakes
    cost_chocolate_cakes = price_chocolate_cake * num_chocolate_cakes

    # L2
    price_strawberry_cake = 22 # $22 each
    num_strawberry_cakes = 6 # 6 strawberry cakes
    cost_strawberry_cakes = price_strawberry_cake * num_strawberry_cakes

    # L3
    total_cost = cost_chocolate_cakes + cost_strawberry_cakes

    # FA
    answer = total_cost
    return answer