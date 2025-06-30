def solve(
    num_roses: int = 25,  # There are 25 roses in a garden
    num_tulips: int = 40,  # There are 40 tulips
    num_daisies: int = 35  # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """
    #: L1
    total_flowers = num_roses + num_tulips + num_daisies # eval: 100 = 25 + 40 + 35
    #: L2
    non_rose_flowers = num_tulips + num_daisies # eval: 75 = 40 + 35
    #: L3
    percentage_non_roses = (non_rose_flowers / total_flowers) * 100 # eval: 75.0 = (75 / 100) * 100
    answer = percentage_non_roses  # FINAL ANSWER # eval: 75.0 = 75.0  # FINAL ANSWER
    return answer # eval: return 75.0