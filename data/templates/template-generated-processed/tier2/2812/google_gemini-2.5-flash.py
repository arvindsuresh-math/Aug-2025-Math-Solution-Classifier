def solve():
    """Index: 2812.
    Returns: the total gain Jewel will make from selling the magazines.
    """
    # L1
    magazine_sell_price = 3.50 # sold at $3.50 each
    magazine_cost = 3 # magazine costs $3 each
    gain_per_magazine = magazine_sell_price - magazine_cost

    # L2
    num_magazines = 10 # bought 10 magazines
    total_gain = gain_per_magazine * num_magazines

    # FA
    answer = total_gain
    return answer