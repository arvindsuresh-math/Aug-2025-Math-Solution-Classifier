def solve(
    num_starfish: int = 7,  # Carly collected 7 starfish
    arms_per_starfish: int = 5,  # each starfish has 5 arms
    num_seastar: int = 1,  # and one seastar
    arms_per_seastar: int = 14  # with 14 arms
):
    """Index: 69.
    Returns: the total number of arms of the animals Carly collected.
    """

    #: L1

    #: L2
    total_arms = arms_per_seastar + arms_per_seastar # eval: 28 = 14 + 14

    #: FA
    answer = total_arms
    return answer # eval: return 28
