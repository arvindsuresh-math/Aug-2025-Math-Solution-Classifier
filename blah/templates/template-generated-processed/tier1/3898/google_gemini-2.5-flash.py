def solve():
    """Index: 3898.
    Returns: the total money Susie earned from selling pizza.
    """
    # L1
    slices_sold = 24 # sell 24 slices of pizza
    price_per_slice = 3 # charges $3 per slice
    earnings_from_slices = slices_sold * price_per_slice

    # L2
    price_per_whole_pizza = 15 # $15 for a whole pizza
    whole_pizzas_sold = 3 # sell 3 whole pizzas
    earnings_from_whole_pizzas = price_per_whole_pizza * whole_pizzas_sold

    # L3
    total_earnings = earnings_from_slices + earnings_from_whole_pizzas

    # FA
    answer = total_earnings
    return answer