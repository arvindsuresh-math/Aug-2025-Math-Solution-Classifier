def solve():
    """Index: 6311.
    Returns: the total bill including shipping.
    """
    # L1
    num_shirts = 3 # 3 shirts
    shirt_price = 12.00 # $12.00 each
    shirts_total_cost = num_shirts * shirt_price

    # L2
    num_shorts = 2 # 2 pairs of shorts
    shorts_price = 15.00 # $15.00 each
    shorts_total_cost = num_shorts * shorts_price

    # L3
    socks_price = 5.00 # a pack of socks for $5.00
    swim_trunks_price = 14.00 # a pair of swim trunks for $14.00
    subtotal_cost = shirts_total_cost + socks_price + shorts_total_cost + swim_trunks_price

    # L4
    shipping_threshold = 50.00 # below $50.00 / above $50.00
    shipping_percent_text = 20 # 20% shipping
    shipping_rate_decimal = 0.20 # 20% of the purchase price for shipping
    shipping_cost = shipping_rate_decimal * subtotal_cost

    # L5
    total_bill = subtotal_cost + shipping_cost

    # FA
    answer = total_bill
    return answer