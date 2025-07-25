def solve():
    """Index: 6523.
    Returns: the total amount John paid for dinner plates and silverware.
    """
    # L1
    silverware_cost = 20 # The silverware cost $20
    dinner_plates_cost_percent = 0.5 # 50% as much as the silverware
    dinner_plates_cost = silverware_cost * dinner_plates_cost_percent

    # L2
    total_cost = dinner_plates_cost + silverware_cost

    # FA
    answer = total_cost
    return answer