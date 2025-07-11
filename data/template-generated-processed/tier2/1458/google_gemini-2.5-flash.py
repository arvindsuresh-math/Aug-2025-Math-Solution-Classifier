def solve():
    """Index: 1458.
    Returns: the total amount of money spent at the restaurant.
    """
    # L1
    num_entrees = 4 # 4 entrees
    cost_per_entree = 20 # $20 each
    total_entree_cost = num_entrees * cost_per_entree

    # L2
    appetizer_cost = 10 # appetizer that costs $10
    total_dinner_cost_before_tip = total_entree_cost + appetizer_cost

    # L3
    tip_percent_decimal = 0.20 # tip 20%
    tip_amount = total_dinner_cost_before_tip * tip_percent_decimal

    # L4
    final_total_cost = total_dinner_cost_before_tip + tip_amount

    # FA
    answer = final_total_cost
    return answer