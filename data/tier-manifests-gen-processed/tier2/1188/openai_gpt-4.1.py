def solve():
    """Index: 1188.
    Returns: the total amount in dollars Preston received for the order.
    """
    # L1
    sandwich_price = 5 # $5 for each sandwich
    num_sandwiches = 18 # 18 sandwiches
    sandwiches_total = sandwich_price * num_sandwiches

    # L2
    delivery_fee = 20 # $20 for a delivery fee
    subtotal = sandwiches_total + delivery_fee

    # L3
    tip_percent = 0.10 # tips him 10%
    tip_amount = subtotal * tip_percent

    # L4
    total_received = subtotal + tip_amount

    # FA
    answer = total_received
    return answer