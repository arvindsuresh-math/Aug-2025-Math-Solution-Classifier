def solve():
    """Index: 703.
    Returns: the number of servings of guacamole Georgie can make.
    """
    # L1
    initial_avocados = 5 # she already had 5 avocados
    bought_avocados = 4 # her sister buys another 4 avocados
    total_avocados = initial_avocados + bought_avocados

    # L2
    avocados_per_serving = 3 # needs 3 avocados to make her grandmother's guacamole recipe
    num_servings = total_avocados / avocados_per_serving

    # FA
    answer = num_servings
    return answer