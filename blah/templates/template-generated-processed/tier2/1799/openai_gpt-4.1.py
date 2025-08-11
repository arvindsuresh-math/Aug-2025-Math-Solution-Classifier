def solve():
    """Index: 1799.
    Returns: the amount Silvia saves by buying from the cheaper store compared to the other store.
    """
    # L1
    retail_price = 1000 # suggested retail price of $1000
    gc_discount_percent_num = 15 # 15% off (Guitar Center)
    percent_factor = 0.01 # WK
    gc_discount_amount = retail_price * gc_discount_percent_num * percent_factor

    # L2
    gc_shipping_fee = 100 # shipping fee of $100 (Guitar Center)
    gc_total_cost = retail_price - gc_discount_amount + gc_shipping_fee

    # L3
    sw_discount_percent_num = 10 # 10% off (Sweetwater)
    sw_discount_amount = retail_price * sw_discount_percent_num * percent_factor

    # L4
    sw_shipping_fee = 0 # free shipping (Sweetwater)
    sw_total_cost = retail_price - sw_discount_amount + sw_shipping_fee

    # L5
    savings = gc_total_cost - sw_total_cost

    # FA
    answer = savings
    return answer