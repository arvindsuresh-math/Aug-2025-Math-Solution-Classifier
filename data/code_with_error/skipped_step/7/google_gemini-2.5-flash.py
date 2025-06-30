def solve(
        initial_jelly_beans_weight: int = 2, # poured into the box enough jelly beans to bring the weight to 2 pounds
        additional_jelly_beans_weight: int = 2 # added another 2 pounds of jelly beans
    ):
    """Index: 7.
    Returns: the final weight of the box of goodies, in pounds.
    """

    #: L1

    #: L2
    weight_after_second_jelly_beans = additional_jelly_beans_weight + additional_jelly_beans_weight

    #: L3
    final_weight = weight_after_second_jelly_beans * 2

    #: FA
    answer = final_weight
    return answer