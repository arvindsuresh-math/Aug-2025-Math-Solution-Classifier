def solve(
    initial_weight: int = 2,  # initial weight after jelly beans poured to bring weight to 2 pounds
    added_jelly_beans: int = 2  # another 2 pounds of jelly beans added later
):
    """Index: 7.
    Returns: the final weight of the box of goodies in pounds.
    """

    #: L1
    weight_after_brownies = 5 # eval: 5 = 5

    #: L2
    weight_after_more_jelly_beans = weight_after_brownies + added_jelly_beans # eval: 7 = 5 + 2

    #: L3
    final_weight = weight_after_more_jelly_beans * 2 # eval: 14 = 7 * 2

    #: FA
    answer = final_weight
    return answer # eval: return 14
