def solve():
    """Index: 2626.
    Returns: the total cost of the slippers with embroidery and shipping.
    """
    # L1
    slippers_price = 50.00 # The slippers are currently $50.00
    discount_percent = 0.10 # 10% off
    slippers_discount = slippers_price * discount_percent

    # L2
    slippers_price_after_discount = slippers_price - slippers_discount

    # L3
    embroidery_per_shoe = 5.50 # embroidery will be $5.50 per shoe
    num_shoes = 2 # 2 shoes make a pair
    embroidery_total = embroidery_per_shoe * num_shoes

    # L4
    shipping_cost = 10.00 # shipping is a flat rate of $10.00
    total_cost = slippers_price_after_discount + embroidery_total + shipping_cost

    # FA
    answer = total_cost
    return answer