def solve():
    """Index: 4822.
    Returns: the total cost for the glasses.
    """
    # L1
    lenses_cost = 500 # lenses cost $500
    insurance_coverage_percent = 0.8 # cover 80% of the cost
    lenses_coverage_amount = lenses_cost * insurance_coverage_percent

    # L2
    final_lenses_cost = lenses_cost - lenses_coverage_amount

    # L3
    frames_cost = 200 # frames cost $200
    coupon_discount = 50 # $50 off coupon
    final_frames_cost = frames_cost - coupon_discount

    # L4
    total_cost = final_lenses_cost + final_frames_cost

    # FA
    answer = total_cost
    return answer