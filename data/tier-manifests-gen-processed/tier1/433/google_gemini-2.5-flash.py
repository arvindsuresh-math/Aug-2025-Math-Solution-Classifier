def solve():
    """Index: 433.
    Returns: the total amount Michael earned from selling paintings.
    """
    # L1
    num_large_paintings = 5 # sold 5 large paintings
    price_large_painting = 100 # charges $100 for a large painting
    earnings_large_paintings = num_large_paintings * price_large_painting

    # L2
    num_small_paintings = 8 # sold 8 small paintings
    price_small_painting = 80 # charges $80 for a small painting
    earnings_small_paintings = num_small_paintings * price_small_painting

    # L3
    total_earnings = earnings_large_paintings + earnings_small_paintings

    # FA
    answer = total_earnings
    return answer