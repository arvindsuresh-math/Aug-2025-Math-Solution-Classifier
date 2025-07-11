def solve():
    """Index: 872.
    Returns: the total amount John spent on pins.
    """
    # L1
    original_price_per_pin = 20 # normally $20 each
    discount_rate = 0.15 # 15% off
    discount_amount_per_pin = original_price_per_pin * discount_rate

    # L2
    price_per_pin_after_discount = original_price_per_pin - discount_amount_per_pin

    # L3
    num_pins = 10 # buy 10 pins
    total_cost = price_per_pin_after_discount * num_pins

    # FA
    answer = total_cost
    return answer