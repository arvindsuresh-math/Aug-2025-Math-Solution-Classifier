def solve():
    """Index: 7223.
    Returns: the money Méliès has left after paying for the meat.
    """
    # L1
    kg_meat_bought = 2 # 2 kg of meat
    cost_per_kg = 82 # $82 per kilogram
    total_meat_cost = kg_meat_bought * cost_per_kg

    # L2
    initial_money = 180 # $180 in his wallet
    money_left = initial_money - total_meat_cost

    # FA
    answer = money_left
    return answer