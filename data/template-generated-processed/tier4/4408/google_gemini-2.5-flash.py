def solve():
    """Index: 4408.
    Returns: the cost of each sandwich.
    """
    # L1
    meat_packs = 2 # 2 packs of sandwich meat
    meat_cost_per_pack = 5.00 # $5.00 per pack
    total_meat_cost = meat_packs * meat_cost_per_pack

    # L2
    cheese_packs = 2 # 2 packs of sliced cheese
    cheese_cost_per_pack = 4.00 # $4.00 per pack
    total_cheese_cost = cheese_packs * cheese_cost_per_pack

    # L3
    bread_cost = 4.00 # The bread costs $4.00
    subtotal_cost = bread_cost + total_meat_cost + total_cheese_cost

    # L4
    coupon_cheese = 1.00 # $1.00 off coupon for one pack of cheese
    coupon_meat = 1.00 # additional $1.00 coupon for one pack of meat
    final_cost_before_per_sandwich = subtotal_cost - coupon_cheese - coupon_meat

    # L5
    num_sandwiches = 10 # make 10 sandwiches
    cost_per_sandwich = final_cost_before_per_sandwich / num_sandwiches

    # FA
    answer = cost_per_sandwich
    return answer