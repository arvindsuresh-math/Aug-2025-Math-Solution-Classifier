def solve():
    """Index: 445.
    Returns: the total amount spent on 2 bags of candy.
    """
    # L1
    bag_original_price = 6.00 # Each bag was $6.00
    discount_percent_num = 75 # 75% off
    discount_percent_decimal = 0.75 # used as .75
    discount_amount = bag_original_price * discount_percent_decimal

    # L2
    bag_price_after_discount = bag_original_price - discount_amount

    # L3
    num_bags = 2 # bought 2 bags
    total_cost = bag_price_after_discount * num_bags

    # FA
    answer = total_cost
    return answer