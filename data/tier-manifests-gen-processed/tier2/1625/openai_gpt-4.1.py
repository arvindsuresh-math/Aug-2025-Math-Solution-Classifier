def solve():
    """Index: 1625.
    Returns: the new price of the movie ticket after a 20% decrease.
    """
    # L1
    last_week_price = 100 # price of a movie ticket was $100
    percent_down = 0.2 # price is down by 20%
    price_decrease = last_week_price * percent_down

    # L2
    new_price = last_week_price - price_decrease

    # FA
    answer = new_price
    return answer