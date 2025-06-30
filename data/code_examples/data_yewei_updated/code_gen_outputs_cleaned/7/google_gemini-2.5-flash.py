def solve(
        initial_jelly_beans_weight: int = 2, # enough jelly beans to bring the weight to 2 pounds
        triple_factor: int = 3, # cause the weight to triple
        additional_jelly_beans_weight: int = 2, # added another 2 pounds of jelly beans
        double_factor: int = 2 # double the weight once again
    ):
    """Index: 7.
    Returns: the final weight of the box of goodies, in pounds.
    """
    #: L1
    weight_after_brownies = initial_jelly_beans_weight * triple_factor

    #: L2
    weight_after_additional_jelly_beans = weight_after_brownies + additional_jelly_beans_weight

    #: L3
    final_weight = weight_after_additional_jelly_beans * double_factor

    answer = final_weight # FINAL ANSWER
    return answer