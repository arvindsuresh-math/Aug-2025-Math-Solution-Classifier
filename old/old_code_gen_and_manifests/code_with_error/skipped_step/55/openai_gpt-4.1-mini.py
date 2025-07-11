def solve(
    num_roses: int = 25,  # There are 25 roses in a garden
    num_tulips: int = 40,  # There are 40 tulips
    num_daisies: int = 35  # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """

    #: L1

    #: L2
    non_rose_flowers = num_tulips + num_daisies

    #: L3
    percentage_non_roses = (non_rose_flowers / num_tulips) * 100

    #: FA
    answer = percentage_non_roses
    return answer