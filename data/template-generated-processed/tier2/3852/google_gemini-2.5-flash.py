def solve():
    """Index: 3852.
    Returns: the total money saved by buying ball bearings during the sale.
    """
    # L1
    ball_bearings_per_machine = 30 # take 30 ball bearings each
    num_machines = 10 # 10 machines
    total_ball_bearings = ball_bearings_per_machine * num_machines

    # L2
    normal_cost_per_bearing = 1 # $1 per ball bearing
    normal_total_cost = total_ball_bearings * normal_cost_per_bearing

    # L3
    sale_cost_per_bearing = 0.75 # only $.75
    cost_after_sale_price = total_ball_bearings * sale_cost_per_bearing

    # L4
    bulk_discount_percent = 0.2 # a further 20% discount
    bulk_discount_amount = cost_after_sale_price * bulk_discount_percent

    # L5
    final_cost_with_discounts = cost_after_sale_price - bulk_discount_amount

    # L6
    total_savings = normal_total_cost - final_cost_with_discounts

    # FA
    answer = total_savings
    return answer