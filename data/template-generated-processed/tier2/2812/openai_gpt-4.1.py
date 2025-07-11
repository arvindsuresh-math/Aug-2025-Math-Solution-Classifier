def solve():
    """Index: 2812.
    Returns: Jewel's total gain from selling the magazines.
    """
    # L1
    sell_price_per_mag = 3.5 # to be sold at $3.50 each
    cost_per_mag = 3 # costs $3 each
    gain_per_mag = sell_price_per_mag - cost_per_mag

    # L2
    num_magazines = 10 # bought 10 magazines
    total_gain = gain_per_mag * num_magazines

    # FA
    answer = total_gain
    return answer