def solve():
    """Index: 3665.
    Returns: the number of quarters needed to buy the items.
    """
    # L1
    candy_bar_cost_cents = 25 # Candy bars cost ¢25
    num_candy_bars = 3 # three candy bars
    total_candy_bar_cost = candy_bar_cost_cents * num_candy_bars

    # L2
    chocolate_cost_cents = 75 # each piece of chocolate costs ¢75
    num_chocolate_pieces = 2 # two pieces of chocolate
    total_chocolate_cost = chocolate_cost_cents * num_chocolate_pieces

    # L3
    juice_cost_cents = 50 # a pack of juice costs ¢50
    total_cost_cents = total_candy_bar_cost + total_chocolate_cost + juice_cost_cents

    # L4
    cents_per_quarter = 25 # a quarter is equal to ¢25
    quarters_needed = total_cost_cents / cents_per_quarter

    # FA
    answer = quarters_needed
    return answer