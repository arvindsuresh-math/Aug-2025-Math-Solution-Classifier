def solve():
    """Index: 673.
    Returns: the amount Johnny pays for the ping pong balls.
    """
    # L1
    num_balls = 10000 # Johnny buys 10000
    cost_per_ball = 0.10 # sell for $.10 each
    total_cost_before_discount = num_balls * cost_per_ball

    # L2
    discount_percent = 0.30 # 30% discount
    discount_amount = total_cost_before_discount * discount_percent

    # L3
    final_payment = total_cost_before_discount - discount_amount

    # FA
    answer = final_payment
    return answer