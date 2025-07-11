def solve():
    """Index: 1063.
    Returns: the grams of sugar in one cupcake.
    """
    # L1
    num_cake_layers = 2 # two-layer cake
    cupcakes_per_dozen = 12 # a dozen cupcakes
    equivalent_cupcakes_from_cake = num_cake_layers * cupcakes_per_dozen

    # L2
    num_cupcakes_made = 12 # a dozen cupcakes
    total_equivalent_cupcakes = equivalent_cupcakes_from_cake + num_cupcakes_made

    # L3
    total_sugar_grams = 720 # Nina used 720 grams of sugar
    sugar_per_cupcake = total_sugar_grams / total_equivalent_cupcakes

    # FA
    answer = sugar_per_cupcake
    return answer