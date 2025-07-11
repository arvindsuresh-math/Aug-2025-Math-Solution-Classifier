def solve():
    """Index: 383.
    Returns: the number of cupcakes Anna has left after giving away and eating some.
    """
    # L1
    total_cupcakes = 60 # Anna baked 60 cupcakes
    divisor = 5 # 4/5 of the cupcakes, so remaining is 1/5
    remaining_cupcakes = total_cupcakes / divisor

    # L2
    cupcakes_eaten = 3 # she eats 3 cupcakes
    cupcakes_left = remaining_cupcakes - cupcakes_eaten

    # FA
    answer = cupcakes_left
    return answer