def solve():
    """Index: 1625.
    Returns: the new price of the movie ticket.
    """
    # L1
    original_price = 100 # price of a movie ticket was $100
    price_decrease_percent = 0.2 # down by 20%
    price_decrease_amount = original_price * price_decrease_percent

    # L2
    new_price = original_price - price_decrease_amount

    # FA
    answer = new_price
    return answer