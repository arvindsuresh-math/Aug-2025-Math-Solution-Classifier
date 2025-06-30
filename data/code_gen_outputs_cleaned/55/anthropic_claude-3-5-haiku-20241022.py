def solve(
        roses: int = 25,  # There are 25 roses in a garden
        tulips: int = 40,  # There are 40 tulips
        daisies: int = 35  # There are 35 daisies
):
    """Index: 55.
    Returns: the percentage of flowers that are not roses."""
    
    #: L1
    total_flowers = roses + tulips + daisies

    #: L2
    non_rose_flowers = tulips + daisies

    #: L3
    percentage_non_roses = (non_rose_flowers / total_flowers) * 100

    answer = percentage_non_roses  # FINAL ANSWER
    return answer