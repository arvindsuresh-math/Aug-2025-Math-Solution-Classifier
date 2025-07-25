def solve(
    initial_jelly_beans_weight: int = 2, # Ken poured into the box enough jelly beans to bring the weight to 2 pounds.
    weight_added_jelly_beans: int = 2, # he added another 2 pounds of jelly beans.
):
    """Index: 7.
    Returns: the final weight of the box of goodies, in pounds.
    """

    #: L1
    weight_after_brownies = initial_jelly_beans_weight * 3

    #: L2
    weight_after_more_jelly_beans = 18

    #: L3
    final_weight = weight_after_more_jelly_beans * 2

    #: FA
    answer = final_weight
    return answer