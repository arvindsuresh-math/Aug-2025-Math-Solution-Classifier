def solve():
    """Index: 3444.
    Returns: the amount of money Josie had left over after buying groceries.
    """
    # L1
    milk_original_cost = 4.00 # a carton of milk for $4.00
    milk_discount_fraction = 0.50 # milk was 1/2 off
    milk_cost_after_discount = milk_original_cost * milk_discount_fraction

    # L2
    banana_pounds = 2 # 2 pounds of bananas
    banana_price_per_pound = 0.75 # $0.75 per pound
    banana_cost = banana_pounds * banana_price_per_pound

    # L3
    detergent_original_cost = 10.25 # a box of laundry detergent for $10.25
    detergent_coupon_value = 1.25 # a coupon for $1.25 off of the laundry detergent
    detergent_cost_after_coupon = detergent_original_cost - detergent_coupon_value

    # L4
    bread_cost = 3.50 # a loaf of bread for $3.50
    total_purchases_cost = milk_cost_after_discount + banana_cost + bread_cost + detergent_cost_after_coupon

    # L5
    initial_bill = 20 # a $20 bill
    money_left_over = initial_bill - total_purchases_cost

    # FA
    answer = money_left_over
    return answer