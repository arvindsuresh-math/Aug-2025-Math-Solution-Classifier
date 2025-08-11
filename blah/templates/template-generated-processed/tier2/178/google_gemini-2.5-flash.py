def solve():
    """Index: 178.
    Returns: the amount of change Simon would receive back from his purchase.
    """
    # L1
    num_pansies = 5 # 5 pansies
    cost_per_pansy = 2.50 # $2.50 each
    pansies_cost = num_pansies * cost_per_pansy

    # L2
    num_petunias = 5 # 5 petunias
    cost_per_petunia = 1.00 # $1.00 each
    petunias_cost = num_petunias * cost_per_petunia

    # L3
    hydrangea_cost = 12.50 # one hydrangea that cost $12.50
    total_initial_cost = pansies_cost + hydrangea_cost + petunias_cost

    # L4
    discount_percent_decimal = 0.10 # 10% off all purchases
    discount_amount = total_initial_cost * discount_percent_decimal

    # L5
    final_purchase_total = total_initial_cost - discount_amount

    # L6
    payment_amount = 50 # $50 bill
    change_received = payment_amount - final_purchase_total

    # FA
    answer = change_received
    return answer