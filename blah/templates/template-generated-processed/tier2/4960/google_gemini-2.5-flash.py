def solve():
    """Index: 4960.
    Returns: the amount of gratuity the waiter should receive in dollars.
    """
    # L1
    dish_price_leticia = 10 # prices for their dishes cost $10
    dish_price_scarlett = 13 # $13
    dish_price_percy = 17 # and $17, respectively
    total_bill = dish_price_leticia + dish_price_scarlett + dish_price_percy

    # L2
    tip_rate = 0.1 # a 10% tip
    total_gratuity = total_bill * tip_rate

    # FA
    answer = total_gratuity
    return answer