def solve():
    """Index: 2132.
    Returns: the cost of one bottle of energy drink.
    """
    # L1
    num_cupcakes = 50 # 50 cupcakes
    price_per_cupcake = 2 # $2 each
    cupcake_earnings = num_cupcakes * price_per_cupcake

    # L2
    num_cookies = 40 # 40 cookies
    price_per_cookie = 0.5 # $0.5 each
    cookie_earnings = num_cookies * price_per_cookie

    # L3
    total_earnings = cupcake_earnings + cookie_earnings

    # L4
    basketball_price = 40 # $40 each
    num_basketballs = 2 # two basketballs
    basketballs_cost = basketball_price * num_basketballs

    # L5
    money_for_drinks = total_earnings - basketballs_cost

    # L6
    num_bottles = 20 # 20 bottles of energy drinks
    price_per_bottle = money_for_drinks / num_bottles

    # FA
    answer = price_per_bottle
    return answer