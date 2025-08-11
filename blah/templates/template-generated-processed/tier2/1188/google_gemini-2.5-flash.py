def solve():
    """Index: 1188.
    Returns: the total amount Preston received.
    """
    # L1
    sandwich_price = 5 # $5 for each sandwich
    num_sandwiches = 18 # 18 sandwiches
    sandwiches_total_price = sandwich_price * num_sandwiches

    # L2
    delivery_fee = 20 # $20 for a delivery fee
    price_with_delivery = sandwiches_total_price + delivery_fee

    # L3
    tip_percent_decimal = 0.10 # tips him 10%
    tip_amount = price_with_delivery * tip_percent_decimal

    # L4
    total_received = price_with_delivery + tip_amount

    # FA
    answer = total_received
    return answer