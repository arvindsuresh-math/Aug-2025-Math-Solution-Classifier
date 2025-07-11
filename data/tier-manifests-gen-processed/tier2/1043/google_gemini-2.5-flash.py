def solve():
    """Index: 1043.
    Returns: the total amount James paid for the living room set.
    """
    # L1
    coach_cost = 2500 # The coach cost $2500
    sectional_cost = 3500 # the sectional cost $3500
    other_cost = 2000 # everything else has a combined cost of $2000
    combined_cost = coach_cost + sectional_cost + other_cost

    # L2
    discount_rate = 0.1 # a 10% discount
    discount_amount = combined_cost * discount_rate

    # L3
    final_payment = combined_cost - discount_amount

    # FA
    answer = final_payment
    return answer