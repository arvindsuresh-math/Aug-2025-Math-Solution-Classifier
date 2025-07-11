def solve():
    """Index: 590.
    Returns: the percentage of each type of chocolate bar in the box.
    """
    # L1
    bars_per_type = 25 # 25 milk chocolate bars, 25 dark chocolate bars, etc.
    num_types = 4 # four types of chocolate bars
    total_bars = bars_per_type * num_types

    # L2
    percentage = 100 # 100 percent in total
    percentage_per_type = percentage / num_types

    # FA
    answer = percentage_per_type
    return answer