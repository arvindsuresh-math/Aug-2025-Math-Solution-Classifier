def solve():
    """Index: 1167.
    Returns: the total amount Daphney will pay for potatoes.
    """
    # L1
    cost_for_2kg = 6 # 2 kg of potatoes costs $6
    quantity_for_cost = 2 # 2 kg of potatoes costs $6
    price_per_kg = cost_for_2kg / quantity_for_cost

    # L2
    total_kg_to_buy = 5 # 5 kg of potatoes
    total_cost = total_kg_to_buy * price_per_kg

    # FA
    answer = total_cost
    return answer