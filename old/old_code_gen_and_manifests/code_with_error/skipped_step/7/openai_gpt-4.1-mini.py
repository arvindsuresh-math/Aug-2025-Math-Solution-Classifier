def solve(
    initial_weight: int = 2,  # initial weight after jelly beans poured to bring weight to 2 pounds
    added_jelly_beans: int = 2  # another 2 pounds of jelly beans added later
):
    """Index: 7.
    Returns: the final weight of the box of goodies in pounds.
    """

    #: L1

    #: L2
    weight_after_more_jelly_beans = added_jelly_beans + added_jelly_beans

    #: L3
    final_weight = weight_after_more_jelly_beans * 2

    #: FA
    answer = final_weight
    return answer