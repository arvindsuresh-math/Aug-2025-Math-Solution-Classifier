def solve(
        initial_jelly_beans_weight: int = 2, # poured into the box enough jelly beans to bring the weight to 2 pounds
        additional_jelly_beans_weight: int = 2 # added another 2 pounds of jelly beans
    ):
    """Index: 7.
    Returns: the final weight of the box of goodies, in pounds.
    """
    #: L1
    weight_after_brownies = initial_jelly_beans_weight * 3 # eval: 6 = 2 * 3
    #: L2
    weight_after_second_jelly_beans = weight_after_brownies + additional_jelly_beans_weight # eval: 8 = 6 + 2
    #: L3
    final_weight = weight_after_second_jelly_beans * 2 # eval: 16 = 8 * 2
    answer = final_weight # FINAL ANSWER # eval: 16 = 16 # FINAL ANSWER
    return answer # eval: return 16