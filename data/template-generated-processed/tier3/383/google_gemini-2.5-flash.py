def solve():
    """Index: 383.
    Returns: the number of cupcakes Anna has left.
    """
    # L1
    total_cupcakes = 60 # Anna baked 60 cupcakes
    remaining_fraction_denominator = 5 # Of the remaining 1/5 of cupcakes
    remaining_cupcakes_after_giving_away = total_cupcakes / remaining_fraction_denominator

    # L2
    eaten_cupcakes = 3 # she eats 3 cupcakes
    cupcakes_left = remaining_cupcakes_after_giving_away - eaten_cupcakes

    # FA
    answer = cupcakes_left
    return answer