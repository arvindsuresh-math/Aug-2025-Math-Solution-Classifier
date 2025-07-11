def solve():
    """Index: 584.
    Returns: the total number of cupcakes Robin ate.
    """
    # L1
    chocolate_sauce = 4 # ate four cupcakes with chocolate sauce
    buttercream_multiplier = 2 # twice as many cupcakes with buttercream frosting
    buttercream = buttercream_multiplier * chocolate_sauce

    # L2
    total = chocolate_sauce + buttercream

    # FA
    answer = total
    return answer