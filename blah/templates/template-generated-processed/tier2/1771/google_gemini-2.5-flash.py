def solve():
    """Index: 1771.
    Returns: the total amount Sophie spends.
    """
    # L1
    num_cupcakes = 5 # five cupcakes
    cost_per_cupcake = 2 # $2 each
    cost_cupcakes = num_cupcakes * cost_per_cupcake

    # L2
    num_doughnuts = 6 # six doughnuts
    cost_per_doughnut = 1 # $1 each
    cost_doughnuts = num_doughnuts * cost_per_doughnut

    # L3
    num_pie_slices = 4 # four slices of apple pie
    cost_per_pie_slice = 2 # $2 per slice
    cost_pie = num_pie_slices * cost_per_pie_slice

    # L4
    num_cookies = 15 # fifteen cookies
    cost_per_cookie = 0.60 # $0.60 each
    cost_cookies = num_cookies * cost_per_cookie

    # L5
    total_spend = cost_cupcakes + cost_doughnuts + cost_pie + cost_cookies

    # FA
    answer = total_spend
    return answer