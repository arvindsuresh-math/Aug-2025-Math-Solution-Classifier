def solve():
    """Index: 1363.
    Returns: Prudence's net profit from selling the remaining cupcakes.
    """
    # L1
    burnt_batches = 2 # first 2 dozen burnt
    good_batches = 2 # next 2 came out perfectly
    evening_batches = 2 # 2 more dozen cupcakes later that day
    total_batches = burnt_batches + good_batches + evening_batches

    # L2
    cupcakes_per_dozen = 12 # WK
    total_cupcakes_made = total_batches * cupcakes_per_dozen

    # L3
    thrown_batches = burnt_batches # She threw away 2 dozen cupcakes
    thrown_cupcakes = thrown_batches * cupcakes_per_dozen

    # L4
    ate_first = 5 # ate 5 cupcakes right away
    ate_later = 4 # ate 4 more later
    cupcakes_left = total_cupcakes_made - thrown_cupcakes - ate_first - ate_later

    # L5
    sale_price_per_cupcake = 2.00 # sells at $2.00 each
    total_earned = cupcakes_left * sale_price_per_cupcake

    # L6
    cost_per_cupcake = 0.75 # cost $0.75 to make each
    total_cost = total_cupcakes_made * cost_per_cupcake

    # L7
    net_profit = total_earned - total_cost

    # FA
    answer = net_profit
    return answer