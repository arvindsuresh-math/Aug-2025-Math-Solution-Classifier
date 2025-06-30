def solve(
    initial_jelly_beans_weight: int = 2, # poured into the box enough jelly beans to bring the weight to 2 pounds
    brownie_multiplier: int = 3, # added enough brownies to cause the weight to triple
    additional_jelly_beans_weight: int = 2, # added another 2 pounds of jelly beans
    gummy_worm_multiplier: int = 2 # added enough gummy worms to double the weight once again
):
    """Index: 7.
    Returns: the final weight of the box of goodies in pounds.
    """

    #: L1
    weight_after_brownies = initial_jelly_beans_weight * brownie_multiplier

    #: L2
    weight_after_additional_jelly_beans = weight_after_brownies + initial_jelly_beans_weight

    #: L3
    final_weight = weight_after_additional_jelly_beans * gummy_worm_multiplier

    #: FA
    answer = final_weight
    return answer