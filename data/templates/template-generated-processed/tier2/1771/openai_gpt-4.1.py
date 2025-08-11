def solve():
    """Index: 1771.
    Returns: the total amount Sophie spends in all.
    """
    # L1
    num_cupcakes = 5 # five cupcakes
    price_per_cupcake = 2 # $2 each
    cupcakes_cost = num_cupcakes * price_per_cupcake

    # L2
    num_doughnuts = 6 # six doughnuts
    price_per_doughnut = 1 # $1 each
    doughnuts_cost = num_doughnuts * price_per_doughnut

    # L3
    num_pie_slices = 4 # four slices of apple pie
    price_per_pie_slice = 2 # $2 per slice
    pie_cost = num_pie_slices * price_per_pie_slice

    # L4
    num_cookies = 15 # fifteen cookies
    price_per_cookie = 0.60 # $0.60 each
    cookies_cost = num_cookies * price_per_cookie

    # L5
    total_spent = cupcakes_cost + doughnuts_cost + pie_cost + cookies_cost

    # FA
    answer = total_spent
    return answer