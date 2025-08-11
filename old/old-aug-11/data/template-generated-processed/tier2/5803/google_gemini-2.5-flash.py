def solve():
    """Index: 5803.
    Returns: the total amount Daniel spends.
    """
    # L1
    magazine_cost = 0.85 # magazine costing $0.85
    pencil_cost = 0.50 # pencil costing $0.50
    total_initial_cost = magazine_cost + pencil_cost

    # L2
    coupon_discount = 0.35 # coupon that gives him $0.35 off
    final_cost = total_initial_cost - coupon_discount

    # FA
    answer = final_cost
    return answer