def solve():
    """Index: 584.
    Returns: the total number of cupcakes Robin ate.
    """
    # L1
    chocolate_cupcakes = 4 # four cupcakes with chocolate sauce
    multiplier_twice = 2 # twice as many cupcakes
    buttercream_cupcakes = multiplier_twice * chocolate_cupcakes

    # L2
    total_cupcakes = chocolate_cupcakes + buttercream_cupcakes

    # FA
    answer = total_cupcakes
    return answer