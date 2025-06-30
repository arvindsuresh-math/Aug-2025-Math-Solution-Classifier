def solve(
    initial_jelly_beans: int = 2,  # Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds
    brownies_multiplier: int = 3,  # he added enough brownies to cause the weight to triple
    additional_jelly_beans: int = 2,  # Next, he added another 2 pounds of jelly beans
    gummy_worms_multiplier: int = 2  # he added enough gummy worms to double the weight once again
):
    """Index: 7.
    Returns: the final weight of the box of goodies in pounds."""

    #: L1
    weight_after_brownies = initial_jelly_beans * brownies_multiplier # eval: 6 = 2 * 3

    #: L2
    weight_after_additional_jelly_beans = weight_after_brownies + additional_jelly_beans # eval: 8 = 6 + 2

    #: L3
    final_weight = weight_after_additional_jelly_beans * gummy_worms_multiplier # eval: 16 = 8 * 2

    #: FA
    answer = final_weight
    return answer # eval: return 16
