def solve():
    """Index: 4937.
    Returns: the total price of buying bananas and oranges.
    """
    # L1
    total_cost_orange_pear = 120 # total cost of an orange and a pear is $120
    cost_pear = 90 # a pear costs $90
    cost_orange = total_cost_orange_pear - cost_pear

    # L2
    cost_banana = cost_pear - cost_orange

    # L3
    num_bananas_to_buy = 200 # 200 bananas
    cost_200_bananas = cost_banana * num_bananas_to_buy

    # L4
    multiplier_oranges = 2 # twice as many oranges
    num_oranges_to_buy = multiplier_oranges * num_bananas_to_buy

    # L5
    cost_oranges = num_oranges_to_buy * cost_orange

    # L6
    total_price = cost_200_bananas + cost_oranges

    # FA
    answer = total_price
    return answer