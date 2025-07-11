def solve():
    """Index: 1326.
    Returns: the original price of each tire.
    """
    # L1
    total_savings = 36 # saved a total of $36
    num_tires = 4 # bought 4 tires
    savings_per_tire = total_savings / num_tires

    # L2
    sale_price_per_tire = 75 # bought 4 tires on sale for $75 each
    original_price_per_tire = sale_price_per_tire + savings_per_tire

    # FA
    answer = original_price_per_tire
    return answer