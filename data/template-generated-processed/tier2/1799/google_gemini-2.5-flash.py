def solve():
    """Index: 1799.
    Returns: the amount Silvia will save by buying from the cheaper store.
    """
    # L1
    suggested_retail_price = 1000 # suggested retail price of $1000
    gc_discount_percent_num = 15 # 15% off
    percent_factor = 0.01 # WK
    gc_discount_amount = suggested_retail_price * gc_discount_percent_num * percent_factor

    # L2
    gc_shipping_fee = 100 # shipping fee of $100
    gc_total_cost = suggested_retail_price - gc_discount_amount + gc_shipping_fee

    # L3
    sw_discount_percent_num = 10 # 10% off deal
    sw_discount_amount = suggested_retail_price * sw_discount_percent_num * percent_factor

    # L4
    sw_shipping_fee = 0 # free shipping
    sw_total_cost = suggested_retail_price - sw_discount_amount + sw_shipping_fee

    # L5
    amount_saved = gc_total_cost - sw_total_cost

    # FA
    answer = amount_saved
    return answer