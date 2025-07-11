def solve():
    """Index: 1363.
    Returns: the net profit from the cupcake business.
    """
    # L1
    burnt_dozens = 2 # The first 2 dozen that she made burnt
    first_cooked_dozens = 2 # The next 2 came out perfectly
    second_cooked_dozens = 2 # made 2 more dozen cupcakes
    total_dozens_made = burnt_dozens + first_cooked_dozens + second_cooked_dozens

    # L2
    cupcakes_per_dozen = 12 # WK
    total_cupcakes_made = total_dozens_made * cupcakes_per_dozen

    # L3
    dozens_burnt = 2 # The first 2 dozen that she made burnt
    cupcakes_thrown_away = dozens_burnt * cupcakes_per_dozen

    # L4
    first_eaten_cupcakes = 5 # eating 5 cupcakes right away
    second_eaten_cupcakes = 4 # decided to eat 4 more
    cupcakes_remaining = total_cupcakes_made - cupcakes_thrown_away - first_eaten_cupcakes - second_eaten_cupcakes

    # L5
    selling_price_per_cupcake = 2.00 # sells the remaining cupcakes at $2.00 each
    total_earned = cupcakes_remaining * selling_price_per_cupcake

    # L6
    cost_per_cupcake = 0.75 # each cupcake cost $0.75 to make
    total_cost_of_making = total_cupcakes_made * cost_per_cupcake

    # L7
    net_profit = total_earned - total_cost_of_making

    # FA
    answer = net_profit
    return answer