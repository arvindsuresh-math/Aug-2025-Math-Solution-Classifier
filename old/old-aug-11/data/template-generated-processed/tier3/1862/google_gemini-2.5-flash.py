def solve():
    """Index: 1862.
    Returns: the number of cousins Jason has.
    """
    # L1
    dozen_value = 12 # WK
    num_dozens = 4 # 4 dozen cupcakes
    total_cupcakes = dozen_value * num_dozens

    # L2
    cupcakes_per_cousin = 3 # give 3 cupcakes each to his cousins
    num_cousins = total_cupcakes / cupcakes_per_cousin

    # FA
    answer = num_cousins
    return answer