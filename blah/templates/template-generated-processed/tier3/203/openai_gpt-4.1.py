def solve():
    """Index: 203.
    Returns: the cost of each candy bar.
    """
    # L1
    num_soft_drinks = 2 # 2 soft drinks
    soft_drink_price = 4 # $4 each
    soft_drinks_total = num_soft_drinks * soft_drink_price

    # L2
    total_spent = 28 # spent a total of 28 dollars
    candy_bars_total = total_spent - soft_drinks_total

    # L3
    num_candy_bars = 5 # 5 candy bars
    candy_bar_price = candy_bars_total / num_candy_bars

    # FA
    answer = candy_bar_price
    return answer