def solve():
    """Index: 2132.
    Returns: the cost of a bottle of energy drink.
    """
    # L1
    num_cupcakes = 50 # 50 cupcakes
    cupcake_price = 2 # $2 each
    cupcake_sales = num_cupcakes * cupcake_price

    # L2
    num_cookies = 40 # 40 cookies
    cookie_price = 0.5 # $0.5 each
    cookie_sales = num_cookies * cookie_price

    # L3
    total_earnings = cupcake_sales + cookie_sales

    # L4
    basketball_price = 40 # $40 each
    num_basketballs = 2 # two basketballs
    basketball_cost = basketball_price * num_basketballs

    # L5
    num_energy_drinks = 20 # 20 bottles of energy drinks
    money_for_energy_drinks = total_earnings - basketball_cost

    # L6
    cost_per_energy_drink = money_for_energy_drinks / num_energy_drinks

    # FA
    answer = cost_per_energy_drink
    return answer