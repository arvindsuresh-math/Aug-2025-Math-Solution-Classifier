def solve():
    """Index: 1273.
    Returns: the total amount John paid for gum and candy bars.
    """
    # L1
    candy_bar_price = 1.5 # the candy bar cost $1.5 each
    gum_price_divisor = 2 # Each stick of gum cost half as much as the candy bar
    gum_price = candy_bar_price / gum_price_divisor

    # L2
    gum_packs = 2 # John buys 2 packs of gum
    gum_total = gum_price * gum_packs

    # L3
    candy_bars = 3 # John buys 3 candy bars
    candy_total = candy_bar_price * candy_bars

    # L4
    total_paid = gum_total + candy_total

    # FA
    answer = total_paid
    return answer