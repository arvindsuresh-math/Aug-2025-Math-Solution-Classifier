def solve():
    """Index: 1043.
    Returns: the total amount James paid after the discount.
    """
    # L1
    coach_cost = 2500 # coach cost $2500
    sectional_cost = 3500 # sectional cost $3500
    other_items_cost = 2000 # everything else has a combined cost of $2000
    total_cost = coach_cost + sectional_cost + other_items_cost

    # L2
    discount_percent = 0.1 # 10% discount
    discount_amount = total_cost * discount_percent

    # L3
    final_payment = total_cost - discount_amount

    # FA
    answer = final_payment
    return answer