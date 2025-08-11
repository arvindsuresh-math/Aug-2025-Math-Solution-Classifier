def solve():
    """Index: 6049.
    Returns: the total cost for Jordyn to buy 50 bags of each fruit with a 10% discount.
    """
    # L1
    discount_percent_num = 10 # 10% discount
    percent_divisor = 100 # WK
    cherry_price_initial = 5 # $5 when the price of a bag of olives is $7
    cherry_discount_amount = (discount_percent_num / percent_divisor) * cherry_price_initial

    # L2
    cherry_price_discounted_per_bag = cherry_price_initial - cherry_discount_amount

    # L3
    num_bags_each_fruit = 50 # buying 50 bags of each fruit
    total_cost_cherries = num_bags_each_fruit * cherry_price_discounted_per_bag

    # L4
    olive_price_initial = 7 # $7
    olive_discount_amount = (discount_percent_num / percent_divisor) * olive_price_initial

    # L5
    olive_price_discounted_per_bag = olive_price_initial - olive_discount_amount

    # L6
    total_cost_olives = olive_price_discounted_per_bag * num_bags_each_fruit

    # L7
    total_cost_both_fruits = total_cost_olives + total_cost_cherries

    # FA
    answer = total_cost_both_fruits
    return answer