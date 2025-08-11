def solve():
    """Index: 4288.
    Returns: the total money Wilson pays after discount.
    """
    # L1
    num_hamburgers = 2 # 2 hamburgers
    price_hamburger = 5 # $5 each
    cost_hamburgers = num_hamburgers * price_hamburger

    # L2
    num_cola = 3 # 3 bottles of cola
    price_cola = 2 # $2 each
    cost_cola = num_cola * price_cola

    # L3
    total_price_before_discount = cost_hamburgers + cost_cola

    # L4
    discount_coupon = 4 # $4 discount coupon
    final_price = total_price_before_discount - discount_coupon

    # FA
    answer = final_price
    return answer