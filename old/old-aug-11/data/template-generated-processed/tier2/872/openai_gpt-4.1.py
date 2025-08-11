def solve():
    """Index: 872.
    Returns: the total amount John spent on pins.
    """
    # L1
    original_price_per_pin = 20 # $20 each
    discount_percent = 0.15 # 15% off
    discount_amount_per_pin = original_price_per_pin * discount_percent

    # L2
    sale_price_per_pin = original_price_per_pin - discount_amount_per_pin

    # L3
    num_pins = 10 # 10 pins
    total_cost = sale_price_per_pin * num_pins

    # FA
    answer = total_cost
    return answer