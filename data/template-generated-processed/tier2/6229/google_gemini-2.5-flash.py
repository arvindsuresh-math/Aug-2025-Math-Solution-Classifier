def solve():
    """Index: 6229.
    Returns: the total cost of the coffee order.
    """
    # L1
    num_drip_coffees = 2 # 2 drip coffees
    cost_per_drip_coffee = 2.25 # $2.25 each
    drip_coffees_cost = num_drip_coffees * cost_per_drip_coffee

    # L2
    num_lattes = 2 # 2 lattes
    cost_per_latte = 4.00 # $4.00
    lattes_cost = num_lattes * cost_per_latte

    # L3
    num_cold_brews = 2 # 2 cold brew coffees
    cost_per_cold_brew = 2.50 # $2.50 each
    cold_brews_cost = num_cold_brews * cost_per_cold_brew

    # L4
    syrup_cost = 0.50 # additional $0.50
    double_shot_espresso_cost = 3.50 # one double shot espresso that’s $3.50
    cappuccino_cost = 3.50 # 1 cappuccino for $3.50
    total_order_cost = drip_coffees_cost + lattes_cost + syrup_cost + cold_brews_cost + double_shot_espresso_cost + cappuccino_cost

    # FA
    answer = total_order_cost
    return answer