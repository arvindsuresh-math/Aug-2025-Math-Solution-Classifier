def solve():
    """Index: 7.
    Returns: the final weight of the box of goodies in pounds.
    """
    # L1
    initial_jelly_beans_weight = 2 # 2 pounds
    brownie_multiplier = 3 # cause the weight to triple
    weight_after_brownies = initial_jelly_beans_weight * brownie_multiplier

    # L2
    added_jelly_beans_weight = 2 # another 2 pounds of jelly beans
    weight_after_second_jelly_beans = weight_after_brownies + added_jelly_beans_weight

    # L3
    gummy_worm_multiplier = 2 # double the weight
    final_weight = weight_after_second_jelly_beans * gummy_worm_multiplier

    # FA
    answer = final_weight
    return answer