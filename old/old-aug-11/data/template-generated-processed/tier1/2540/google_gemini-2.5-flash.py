def solve():
    """Index: 2540.
    Returns: the amount of money the art piece will have increased by.
    """
    # L1
    initial_price = 4000 # purchased an art piece for $4000
    price_multiplier = 3 # three times as much
    future_price = price_multiplier * initial_price

    # L2
    increase_amount = future_price - initial_price

    # FA
    answer = increase_amount
    return answer