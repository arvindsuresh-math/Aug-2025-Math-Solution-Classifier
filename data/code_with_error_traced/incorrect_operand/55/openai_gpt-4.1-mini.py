def solve(
    num_roses: int = 25,  # There are 25 roses in a garden
    num_tulips: int = 40,  # There are 40 tulips
    num_daisies: int = 35  # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """

    #: L1
    total_flowers = num_tulips + num_tulips + num_daisies # eval: 115 = 40 + 40 + 35

    #: L2
    non_rose_flowers = num_tulips + num_daisies # eval: 75 = 40 + 35

    #: L3
    percentage_non_roses = (non_rose_flowers / total_flowers) * 100 # eval: 65.21739130434783 = (75 / 115) * 100

    #: FA
    answer = percentage_non_roses
    return answer # eval: return 65.21739130434783
