def solve(
        roses: int = 25,  # There are 25 roses in a garden
        tulips: int = 40,  # There are 40 tulips
        daisies: int = 35  # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses."""

    #: L1
    total_flowers = roses + tulips + daisies # eval: 100 = 25 + 40 + 35

    #: L2
    non_rose_flowers = tulips + daisies # eval: 75 = 40 + 35

    #: L3
    percentage_non_roses = (non_rose_flowers / total_flowers) * 100 # eval: 75.0 = (75 / 100) * 100

    #: FA
    answer = percentage_non_roses # eval: 75.0 = 75.0
    return answer # eval: return 75.0
