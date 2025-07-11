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

    #: FA
    answer = daisies
    return answer # eval: return 35
