def solve():
    """Index: 1458.
    Returns: the total amount of money spent at the restaurant including tip.
    """
    # L1
    num_entrees = 4 # 4 entrees
    entree_cost = 20 # $20 each
    total_entree_cost = num_entrees * entree_cost

    # L2
    appetizer_cost = 10 # appetizer that costs $10
    dinner_total = total_entree_cost + appetizer_cost

    # L3
    tip_percent = 0.20 # tip 20% of the total
    tip_amount = dinner_total * tip_percent

    # L4
    total_with_tip = dinner_total + tip_amount

    # FA
    answer = total_with_tip
    return answer