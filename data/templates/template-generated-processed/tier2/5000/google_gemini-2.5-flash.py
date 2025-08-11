def solve():
    """Index: 5000.
    Returns: the total grocery bill.
    """
    # L1
    num_veg_bags = 4 # 4 bags of frozen vegetables
    cost_per_veg_bag = 2.00 # $2.00 per bag
    total_veg_cost = num_veg_bags * cost_per_veg_bag

    # L2
    meat_cost = 5.00 # hamburger meat for $5.00
    crackers_cost = 3.50 # box of crackers for $3.50
    cheese_cost = 3.50 # pack of cheese for $3.50
    subtotal_before_discount = meat_cost + crackers_cost + total_veg_cost + cheese_cost

    # L3
    discount_percent_num = 10 # 10% off
    discount_percent_decimal = 0.10 # .10*20
    discount_amount = discount_percent_decimal * subtotal_before_discount

    # L4
    final_bill = subtotal_before_discount - discount_amount

    # FA
    answer = final_bill
    return answer