def solve(
        roses: int = 25, # 25 roses
        tulips: int = 40, # 40 tulips
        daisies: int = 35 # 35 daisies
    ):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """
    #: L1
    total_flowers = roses + tulips + daisies

    #: L2
    flowers_not_roses = tulips + daisies

    #: L3
    percentage_not_roses = (flowers_not_roses / total_flowers) * 100

    answer = percentage_not_roses # FINAL ANSWER
    return answer