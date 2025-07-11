def solve():
    """Index: 7.
    Returns: the final weight of the box of goodies, in pounds.
    """
    # L1
    initial_jelly_beans = 2 # bring the weight to 2 pounds
    tripling_factor = 3 # cause the weight to triple
    after_brownies = initial_jelly_beans * tripling_factor

    # L2
    added_jelly_beans = 2 # added another 2 pounds of jelly beans
    after_second_jelly_beans = after_brownies + added_jelly_beans

    # L3
    doubling_factor = 2 # double the weight once again
    final_weight = after_second_jelly_beans * doubling_factor

    # FA
    answer = final_weight
    return answer