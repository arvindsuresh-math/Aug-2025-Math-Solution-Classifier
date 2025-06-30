def solve(
        roses: int = 25, # 25 roses
        tulips: int = 40, # 40 tulips
        daisies: int = 35 # 35 daisies
    ):
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """
    #: L1
    total_flowers = roses + tulips + daisies # eval: 100 = 25 + 40 + 35
    #: L2
    flowers_not_roses = tulips + daisies # eval: 75 = 40 + 35
    #: L3
    percentage_not_roses = (flowers_not_roses / total_flowers) * 100 # eval: 75.0 = (75 / 100) * 100
    answer = percentage_not_roses # FINAL ANSWER # eval: 75.0 = 75.0 # FINAL ANSWER
    return answer # eval: return 75.0