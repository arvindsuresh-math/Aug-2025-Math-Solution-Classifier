def solve():
    """Index: 257.
    Returns: the amount of money Hannah has left after her purchases.
    """
    # L1
    num_cookies = 40 # 40 pieces of cookies
    price_per_cookie = 0.8 # $0.8 each
    cookie_earnings = num_cookies * price_per_cookie

    # L2
    num_cupcakes = 30 # 30 cupcakes
    price_per_cupcake = 2 # $2 each
    cupcake_earnings = num_cupcakes * price_per_cupcake

    # L3
    total_earnings = cookie_earnings + cupcake_earnings

    # L4
    num_spoon_sets = 2 # 2 sets of measuring spoons
    price_per_spoon_set = 6.5 # $6.5 each
    total_spoon_cost = num_spoon_sets * price_per_spoon_set

    # L5
    answer = total_earnings - total_spoon_cost
    return answer