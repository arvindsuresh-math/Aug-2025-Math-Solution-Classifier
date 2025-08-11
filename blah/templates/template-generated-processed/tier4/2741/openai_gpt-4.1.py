def solve():
    """Index: 2741.
    Returns: the number of candy bars Zoe needs to sell to earn the money for the trip.
    """
    # L1
    trip_cost = 485 # the cost is $485
    grandma_contribution = 250 # Her grandma gave her $250
    amount_needed = trip_cost - grandma_contribution

    # L2
    earnings_per_bar = 1.25 # She makes $1.25 for every candy bar
    num_candy_bars = amount_needed / earnings_per_bar

    # FA
    answer = num_candy_bars
    return answer