def solve():
    """Index: 2741.
    Returns: the number of candy bars Zoe needs to sell.
    """
    # L1
    total_cost = 485 # cost is $485
    grandma_contribution = 250 # grandma gave her $250
    remaining_cost = total_cost - grandma_contribution

    # L2
    earnings_per_candy_bar = 1.25 # makes $1.25 for every candy bar she sells
    candy_bars_needed = remaining_cost / earnings_per_candy_bar

    # FA
    answer = candy_bars_needed
    return answer