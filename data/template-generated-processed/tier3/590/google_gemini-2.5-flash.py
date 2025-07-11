def solve():
    """Index: 590.
    Returns: the percentage of each type of chocolate bar.
    """
    # L1
    bars_per_type = 25 # 25 milk chocolate bars, 25 dark chocolate bars, 25 milk chocolate with almond bars, and 25 white chocolate bars
    num_types = 4 # four types of chocolate bars
    total_bars = bars_per_type * num_types

    # L2
    percentage_per_type = total_bars / num_types

    # FA
    answer = percentage_per_type
    return answer